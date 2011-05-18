"""Patches to resource registries
"""

from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName
from Products.ResourceRegistries import permissions
from zope.app.event.objectevent import ObjectModifiedEvent
from zope.event import notify


security = ClassSecurityInfo()
security.declareProtected(permissions.ManagePortal, 'manage_saveStylesheets')
def manage_saveStylesheets(self, REQUEST=None):
    """Save stylesheets from the ZMI.

    Updates the whole sequence. For editing and reordering.
    """
    self.original_manage_saveStylesheets(REQUEST)
    notify(ObjectModifiedEvent(self))
    if REQUEST:
        portal_url = getToolByName(self, 'portal_url')()
        return REQUEST.RESPONSE.redirect(portal_url + 
                '/@@invalidateClientsCache')


security.declareProtected(permissions.ManagePortal, 'manage_saveScripts')
def manage_saveScripts(self, REQUEST=None):
    """Save scripts from the ZMI.

    Updates the whole sequence. For editing and reordering.
    """

    self.original_manage_saveScripts(REQUEST)
    notify(ObjectModifiedEvent(self))
    if REQUEST:
        portal_url = getToolByName(self, 'portal_url')()
        return REQUEST.RESPONSE.redirect(portal_url + 
                '/@@invalidateClientsCache')

