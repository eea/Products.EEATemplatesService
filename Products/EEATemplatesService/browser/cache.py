import urllib

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.interface import implements
from interfaces import IClientsCache
from Products.CMFSquidTool.queue import queue
from Products.CMFSquidTool.utils import pruneUrl

class ClientsCache(BrowserView):

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
            squid = getToolByName(self.context, 'portal_squid')
            purge_urls = squid.computePurgeUrls(ts_props.getProperty('template_urls', []))
            for url in purge_urls:
                status, xcache, xerror = pruneUrl(url, 'PURGE')
                report += 'squid: %s\r\n' % url
                
            for url in ts_props.getProperty('external_urls', []):
                try:
                    f = urllib.urlopen(url)
                    report += 'Cache invalidated. URL: %s\r\n' % url
                except:
                    report += 'Failed to invalidate cache, URL: %s\r\n' % url

        return report

