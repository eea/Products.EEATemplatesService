""" Cache module
"""
import urllib
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.interface import implements
from Products.EEATemplatesService.browser.interfaces import IClientsCache
#TODO: plone4
#from Products.CMFSquidTool.utils import pruneUrl

class ClientsCache(BrowserView):
    """ ClientsCache BrowserView
    """
    implements(IClientsCache)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        props = getToolByName(self.context, 'portal_properties')
        ts_props = getattr(props, 'template_service', None)
        report = ''

        # don't fail if EEATemplateService profile and config is not loaded
        if ts_props is not None:
            #TODO: fix me, we dont use portal_squid anymore, plone4
            #squid = getToolByName(self.context, 'portal_squid')
            #purge_urls = squid.computePurgeUrls(
                            #ts_props.getProperty('template_urls', []))
            #for url in purge_urls:
                #_status, _xcache, _xerror = pruneUrl(url, 'PURGE')
                #report += 'squid: %s\r\n' % url

            for url in ts_props.getProperty('external_urls', []):
                try:
                    urllib.urlopen(url)
                    report += 'Cache invalidated. URL: %s\r\n' % url
                except IOError:
                    report += 'Failed to invalidate cache, URL: %s\r\n' % url

        return report
