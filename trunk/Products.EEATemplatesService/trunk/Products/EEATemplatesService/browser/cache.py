""" Cache module
"""
import urllib
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.interface import implements
from Products.EEATemplatesService.browser.interfaces import IClientsCache

try:
    from plone.cachepurging.interfaces import IPurger
    from plone.cachepurging.interfaces import IPurgePathRewriter
    from plone.cachepurging.interfaces import ICachePurgingSettings
    from plone.registry.interfaces import IRegistry
    from zope.component import getUtility, queryUtility
    PLONE_APP_CACHING_INSTALLED = True
except ImportError:
    PLONE_APP_CACHING_INSTALLED = False

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

        # Don't fail if EEATemplateService profile and config is not loaded
        if ts_props is not None:
            external_urls = ts_props.getProperty('external_urls', [])
            template_urls = ts_props.getProperty('template_urls', [])

            if PLONE_APP_CACHING_INSTALLED:
                registry = queryUtility(IRegistry)
                if registry:
                    settings = registry.forInterface(ICachePurgingSettings,
                                                     check=False)
                    purger = getUtility(IPurger)
                    rewriter = IPurgePathRewriter(self.request, None)
                    caching_proxies = settings.cachingProxies

                    if caching_proxies:
                        for template_url in template_urls:
                            paths_to_purge = rewriter(template_url)
                            for path_to_purge in paths_to_purge:
                                for caching_proxy in caching_proxies:
                                    full_path = '%s%s' % (caching_proxy,
                                                          path_to_purge)
                                    purger.purgeAsync(full_path)
                                    report += 'Varnish purged: %s\r\n' % \
                                                                    full_path

            for url in external_urls:
                try:
                    urllib.urlopen(url)
                    report += 'Cache invalidated. URL: %s\r\n' % url
                except IOError:
                    report += 'Failed to invalidate cache, URL: %s\r\n' % url

        return report
