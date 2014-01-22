#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gw_backend_redis.example
~~~~~~~~~~~~~~~~~~~~~~~~

Stati example to use Redis pub/sub transport

:copyright: (c) 2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/gottwall-backend-redis
"""


STORAGE = 'gottwall.storages.MemoryStorage'

BACKENDS = {
    'gw_backend_redis.backend.RedisBackend': {
        'HOST': "127.0.0.1",
        'PORT': 6379,
        'PASSWORD': None,
        'DB': 2,
        "CHANNEL": "gottwall"},
    }

TEMPLATE_DEBUG = True

STORAGE_SETTINGS = dict(
    HOST = 'localhost',
    PORT = 6379,
    PASSWORD = None,
    DB = 2
)

REDIS = {"CHANNEL": "gottwall"}


USERS = ["alexandr.s.rus@gmail.com"]

SECRET_KEY = "dwefwefwefwecwef"

# http://public_key:secret_key@host.com

PROJECTS = {"test_project": "my_public_key",
            "another_project": "public_key2"}

cookie_secret="fkewrlhfwhrfweiurbweuybfrweoubfrowebfioubweoiufbwbeofbowebfbwup2XdTP1o/Vo="

TEMPLATE_DEBUG = True


DATABASE = {
    "ENGINE": "postgresql+psycopg2",
    "HOST": "localhost",
    "PORT": 5432,
    "USER": "postgres",
    "PASSWORD": "none",
    "NAME": "gottwall"
    }

PREFIX = ""
