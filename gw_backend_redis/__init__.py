#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
gw_backend_redis
~~~~~~~~~~~~~~~~

GottWall redis transport.

:copyright: (c) 2012 - 2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
:github: http://github.com/GottWall/gottwall-backend-redis
"""

__all__ = 'get_version', 'Client'
__author__ = "Alex Lispython (alex@obout.ru)"
__license__ = "BSD, see LICENSE for more details"
__maintainer__ = "Alexandr Lispython"

try:
    __version__ = __import__('pkg_resources') \
        .get_distribution('gw_backend_redis').version
except Exception, e:
    __version__ = 'unknown'

if __version__ == 'unknown':
    __version_info__ = (0, 0, 0)
else:
    __version_info__ = __version__.split('.')
__build__ = 0x00001


from gw_backend_redis.backend import RedisBackend
from gw_backend_redis.processing import RedisBackendPeriodicProcessor

assert RedisBackend
assert RedisBackendPeriodicProcessor


def get_version():
    return __version__
