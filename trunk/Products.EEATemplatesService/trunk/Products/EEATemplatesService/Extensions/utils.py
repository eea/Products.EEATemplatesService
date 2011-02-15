from Globals import package_home
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.utils import getToolByName
import os, string


def getSkinsFolderNames(globals, skins_dir='skins'):
    # Get the content of the skins folder
    skins_path = os.path.join(package_home(globals), skins_dir)
    return [ filename for filename in os.listdir(skins_path)
        if (not filename.startswith('.') or filename in ('CVS', '{arch}'))
        and os.path.isdir(os.path.join(skins_path, filename)) ]

def setupSkin(self, out, globals, skin_selection, make_default,
                         allow_any, cookie_persistence, skins_dir='skins'):
    skins_tool = getToolByName(self, 'portal_skins')
    skin_name, base_skin = skin_selection['name'], skin_selection['base']

    # Only add the skin selection if it doesn't already exist
    if skin_name not in skins_tool.getSkinSelections():

        # Get the skin layers of the base skin and convert to an array
        layers = skins_tool.getSkinPath(base_skin)
        layers = map(string.strip, string.split(layers, ','))

        # Add the skin folders to the layers, under 'custom'
        filenames = skin_selection.get('layers',
                                     getSkinsFolderNames(globals, skins_dir))
        for filename in filenames:
            if filename not in layers:
                try:
                    layers.insert(layers.index('custom')+1, filename)
                except ValueError:
                    layers.insert(0, filename)

        # Add our skin selection
        layers = ', '.join(layers)
        skins_tool.addSkinSelection(skin_name, layers)
        print >> out, "Added skin selection to portal_skins."

        # Activate the skin selection
        if make_default:
            skins_tool.default_skin = skin_name

        # Setup other tool properties
        skins_tool.allow_any = allow_any
        skins_tool.cookie_persistence = cookie_persistence

    else:
        print >> out, "Skin selection already exists, leaving it alone."

def setupSkins(self, out, globals, skin_selections, select_skin, default_skin,
                          allow_any, cookie_persistence, skins_dir='skins'):
    skins_tool = getToolByName(self, 'portal_skins')

    # Add directory views
    addDirectoryViews(skins_tool, skins_dir, globals)
    print >> out, "Added directory views to portal_skins."

    # Install skin selections
    for skin in skin_selections:
        make_default = False
        if select_skin and skin['name'] == default_skin:
            make_default = True
        setupSkin(self, out, globals, skin, make_default,
                                   allow_any, cookie_persistence, skins_dir)

def updateResources(tool, updates):
    resources = list(tool.resources)
    # This could probably be optimized
    for update in updates:
        for resource in resources:
            if resource.getId() == update['id']:
                if update.has_key('expression') and \
                            hasattr(resource, 'setExpression'):
                    resource.setExpression(update['expression'])
                if update.has_key('media') and \
                            hasattr(resource, 'setMedia'):
                    resource.setMedia(update['media'])
                if update.has_key('rel') and \
                            hasattr(resource, 'setRel'):
                    resource.setRel(update['rel'])
                if update.has_key('title') and \
                            hasattr(resource, 'setTitle'):
                    resource.setTitle(update['title'])
                if update.has_key('rendering') and \
                            hasattr(resource, 'setRendering'):
                    resource.setRendering(update['rendering'])
                if update.has_key('enabled') and \
                            hasattr(resource, 'setEnabled'):
                    resource.setEnabled(update['enabled'])
                if update.has_key('cookable') and \
                            hasattr(resource, 'setCookable'):
                    resource.setCookable(update['cookable'])
                if update.has_key('cacheable') and \
                            hasattr(resource, 'setCacheable'):
                    resource.setCacheable(update['cacheable'])
                if update.has_key('inline') and \
                            hasattr(resource, 'setInline'):
                    resource.setInline(update['inline'])
                break
        tool.resources = tuple(resources)
        tool.cookResources()

def registerStylesheets(self, out, stylesheets):
    # register additional CSS stylesheets with portal_css
    csstool = getToolByName(self, 'portal_css')
    existing = csstool.getResourceIds()
    updates = []
    for css in stylesheets:
        if css.get('id') not in existing:
            csstool.registerStylesheet(**css)
        else:
            updates.append(css)
    if updates:
        updateResources(csstool, updates)
    print >> out, "installed the Plone additional stylesheets."

def registerScripts(self, out, scripts):
    # register additional JS Scripts with portal_javascripts
    jstool = getToolByName(self, 'portal_javascripts')
    existing = jstool.getResourceIds()
    updates = []
    for js in scripts:
        if not js.get('id') in existing:
            jstool.registerScript(**js)
        else:
            updates.append(js)
    if updates:
        updateResources(jstool, updates)            
    print >> out, "installed the Plone additional javascripts."

def removeSkins(self, out, skin_selections, default, fullreset):
    # Delete the portal_skins properties which hold the skins selections
    skins_tool = getToolByName(self, 'portal_skins')

    # Remove skin selections from portal_skins
    for skin in skin_selections:
        skin_name = skin['name']
        if skin_name in skins_tool.getSkinSelections():
            skins_tool.manage_skinLayers(del_skin=1, chosen=(skin_name,))
            print >> out, \
                "Removed skin selection '%s' from portal skins." %skin_name

    # Set Skins Tool parameters back to defaults
    if fullreset:
        # Restore Plone defaults
        skins_tool.allow_any = 0
        skins_tool.cookie_persistence = 0
        selection = 'Plone Default'
    else:
        # Select the base of the default skin selection in the skins tool
        if default:
            selection = [ s for s in skin_selections
                          if s['name'] == default ][0]['base']
        else:
            selection = skin_selections[0]['base']
    skins_tool.default_skin = selection

__all__ = (
    "setupSkins",
    "registerStylesheets",
    "registerScripts",
    "removeSkins",
        )
