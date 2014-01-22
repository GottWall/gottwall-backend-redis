#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
gw_backend_redis.tests
~~~~~~~~~~~~~~~~~~~~~~

Unittests for gottwall backend redis

:copyright: (c) 2012 - 2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/gottwall-backend-redis
"""
import datetime
import json
import os
import random
import gottwall.default_config
import tornado.gen
import tornadoredis
from gottwal.utils.tests import async_test
from gottwall.aggregator import AggregatorApplication
from gottwall.config import Config
from gottwall.utils.tests import AsyncHTTPBaseTestCase
from tornado import ioloop


HOST = os.environ.get('GOTTWALL_REDIS_HOST', "10.8.9.9")


class TestRedisClient(tornadoredis.Client):

    def __init__(self, *args, **kwargs):
        self._on_destroy = kwargs.get('on_destroy', None)
        if 'on_destroy' in kwargs:
            del kwargs['on_destroy']
        super(TestRedisClient, self).__init__(*args, **kwargs)

    def __del__(self):
        super(TestRedisClient, self).__del__()
        if self._on_destroy:
            self._on_destroy()


class RedisTestCaseMixin(object):

    def setUp(self):
        super(RedisTestCaseMixin, self).setUp()
        self.client = self._new_client()
        self.client.flushdb()

    def tearDown(self):
        try:
            self.client.connection.disconnect()
            del self.client
        except AttributeError:
            pass
        super(RedisTestCaseMixin, self).tearDown()


    def _new_client(self, pool=None, on_destroy=None):
        client = TestRedisClient(io_loop=self.io_loop,
                                 host=self.redis_settings['HOST'],
                                 port=self.redis_settings['PORT'],
                                 selected_db=self.redis_settings['DB'],
                                 connection_pool=pool,
                                 on_destroy=on_destroy)

        return client



class RedisBackendTestCase(AsyncHTTPBaseTestCase, RedisTestCaseMixin):

    def setUp(self):
        super(RedisBackendTestCase, self).setUp()
        self.client = self._new_client()
        self.client.flushdb()

    def tearDown(self):
        try:
            self.client.connection.disconnect()
            del self.client
        except AttributeError:
            pass
        super(RedisBackendTestCase, self).tearDown()

    def get_new_ioloop(self):
        return ioloop.IOLoop.instance()

    def get_app(self):
        config = Config()
        config.from_module(gottwall.default_config)

        config.update({"BACKENDS": {"gw_backends_redis.backends.redis.RedisBackend": {"HOST": HOST}},
                       "STORAGE": "gottwall.storages.MemoryStorage",
                       "REDIS_HOST": HOST,
                       "PROJECTS": {"test_project": "secretkey2"},
                       "SECRET_KEY": "myprivatekey2"})
        app = AggregatorApplication(config)
        app.configure_app(self.io_loop)
        return app

    @async_test
    @tornado.gen.engine
    def test_subscribe(self):
        app = self.get_app()
        metric_data = {"name": "redis_metric_{0}".format(random.randint(1, 10)),
                       "timestamp": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
                       "filters": {"views": "anonymouse"},
                       "action": "incr",
                       "value": 2,
                       "type": "bucket"}

        client = self.client
        key = "gottwall:{0}:{1}:{2}".format("test_project",
                                            app.config['PROJECTS']['test_project'],
                                            app.config['SECRET_KEY'])

        (yield tornado.gen.Task(client.publish, key,
                                json.dumps(metric_data)))

        self.stop()
