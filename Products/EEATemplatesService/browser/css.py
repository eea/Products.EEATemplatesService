""" Css packed
"""
from App.Common import rfc1123_date
from DateTime import DateTime
from zope.component import getMultiAdapter
from zope.interface import directlyProvidedBy, directlyProvides
from zope.publisher.browser import TestRequest
from Products.CMFCore.utils import getToolByName
from Products.ResourceRegistries.tools.packer import CSSPacker


class CSS(object):
    """ Handle criteria
    """
    def __init__(self, context, request, resources=()):
        self.context = context
        self.request = request
        self._resources = resources
        self.duration = 3600*24*365

        self.csstool = getToolByName(context, 'portal_css')
        self.pprops = getToolByName(context, 'portal_properties')
        self.debug = self.csstool.getDebugMode()

    @property
    def resources(self):
        """ Return resources
        """
        return self._resources

    def get_resource(self, resource):
        """ Get resource content
        """
        content = self.csstool.getResourceContent(resource, self.context)
        return content

    def get_content(self, **kwargs):
        """ Get content
        """
        output = []
        for resource in self.resources:
            content = self.get_resource(resource)
            if not self.debug:
                content = CSSPacker('safe').pack(content)
            output.append(content)
        return '\n'.join(output)


class ViewCSS(CSS):
    """ CSS libs used in view mode
    """
    @property
    def css_libs(self):
        """ CSS Libs
        """
        fallback = ['ploneCustom.css']
        tservice = getattr(self.pprops, 'template_service')
        val = getattr(tservice, 'css_libs')
        return val or fallback

    @property
    def resources(self):
        """ Return view resources
        """
        return self.css_libs

    def __call__(self, *args, **kwargs):
        """ view.css
        """
        self.request.RESPONSE.setHeader('content-type', 'text/css')
        expires = rfc1123_date((DateTime() + 365).timeTime())
        self.request.RESPONSE.setHeader('Expires', expires)
        self.request.RESPONSE.setHeader(
            'Cache-Control', 'max-age=%d' % self.duration)
        return self.get_content()


