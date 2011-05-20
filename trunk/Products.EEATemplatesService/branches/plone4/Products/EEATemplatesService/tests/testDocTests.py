""" DocTests
"""
from Products.EEATemplatesService.tests import base
import unittest
from zope.testing import doctest
from Testing.ZopeTestCase import FunctionalDocFileSuite

#TODO: fix me, plone4
#import time
#from Products.CMFCore.utils import getToolByName
#from Products.CMFSquidTool.utils import stopThreads
#from Products.CMFSquidTool.tests.test_connections import start_proxied_server

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

class CacheTestCase(base.EEATemplatesService):
    """ CacheTestCase test class
    """

    #TODO: we dont use Products.CMFSquidTool anymore, plone4
    #def afterSetUp(self):
        #""" afterSetUp test method
        #"""
        #self.setRoles(['Manager'])
        #cacheTool = getToolByName(self.portal, 'portal_cache_settings', None)
        #cacheTool.setProxyPurgeConfig('custom-rewrite')
        #cacheTool.setSquidURLs(['http://127.0.0.1:3128'])
        #cacheTool.setDomains(['http://nohost:80'])
        #cacheTool.setEnabled(True)
        #squidTool = getToolByName(self.portal, 'portal_squid', None)
        #squidTool.setUrlExpression(
                #'python:object.portal_cache_settings.getUrlsToPurge(object)')
        #self.httpd, self.httpt = start_proxied_server()

    #def beforeTearDown(self):
        #""" beforeTearDown test method
        #"""
        #try:
            ## If anything remains in our response queue, it means the test
            ## failed (but - we give it a little time to stop.)
            #if self.httpd is not None:
                #for _i in range(10):
                    #if self.httpd.response_queue.empty():
                        #break
                    #time.sleep(0.1)
                #self.failUnless(
                        #self.httpd.response_queue.empty(),
                            #"response queue not consumed")
            #if not stopThreads(wait=True):
                #self.fail("The purge threads did not stop")
        #finally:
            #if self.httpd is not None:
                #self.httpd.stop()
                #self.httpt.join(5)
                #self.httpd = None
                #self.httpt = None

def test_suite():
    """ main test_suite function
    """
    return unittest.TestSuite((
        FunctionalDocFileSuite('cache.txt',
                     test_class = CacheTestCase,
                     package = 'Products.EEATemplatesService.browser',
                     optionflags= OPTIONFLAGS, ), ))
