# -*- coding: utf-8 -*-

import base
import unittest
from zope.testing import doctest

from Products.CMFCore.utils import getToolByName
from Products.CMFSquidTool.utils import stopThreads
from Products.CMFSquidTool.tests.test_connections import start_proxied_server
import time

class CacheTestCase(base.EEATemplatesService):
    
    def afterSetUp(self):
        self.setRoles(['Manager'])
        cacheTool = getToolByName(self.portal, 'portal_cache_settings', None)
        cacheTool.setProxyPurgeConfig('custom-rewrite')
        cacheTool.setSquidURLs(['http://127.0.0.1:3128'])
        cacheTool.setDomains(['http://nohost:80'])
        cacheTool.setEnabled(True)
        squidTool = getToolByName(self.portal, 'portal_squid', None)        
        squidTool.setUrlExpression('python:object.portal_cache_settings.getUrlsToPurge(object)')
        self.httpd, self.httpt = start_proxied_server()
        
    def beforeTearDown(self):
        try:
            # If anything remains in our response queue, it means the test
            # failed (but - we give it a little time to stop.)
            if self.httpd is not None:
                for i in range(10):
                    if self.httpd.response_queue.empty():
                        break
                    time.sleep(0.1)
                self.failUnless(self.httpd.response_queue.empty(), "response queue not consumed")
            if not stopThreads(wait=True):
                self.fail("The purge threads did not stop")
        finally:
            if self.httpd is not None:
                self.httpd.stop()
                self.httpt.join(5)
                self.httpd = None
                self.httpt = None

def test_suite():
    from Testing.ZopeTestCase import FunctionalDocFileSuite

    return unittest.TestSuite((
        FunctionalDocFileSuite('cache.txt',
                     test_class = CacheTestCase,
                     package = 'Products.EEATemplatesService.browser',
                     optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
                     ),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
