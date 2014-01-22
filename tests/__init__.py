#!/usr/bin/env python
# -*- coding:  utf-8 -*-
"""
gw_backend_redis.tests
~~~~~~~~~~~~~~~~~~~~~~

Unittests for gw_backend_redis

:copyright: (c) 2012-2014 by GottWall team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

import sys
sys.path.append("/github/libs/gottwall/")

import unittest
from backends import RedisBackendTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RedisBackendTestCase))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest="suite")
