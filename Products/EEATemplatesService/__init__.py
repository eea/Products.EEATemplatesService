# Register our skins directory - this makes it available via portal_skins.

from Products.CMFCore.DirectoryView import registerDirectory
from Products.GenericSetup import EXTENSION, profile_registry
from Products.CMFPlone.interfaces import IPloneSiteRoot

profile_registry.registerProfile(
                    'default',
                    'EEATemplatesService',
                    'Extension profile with EEA workflows and content types',
                    'profiles/default',
                    'EEATemplatesService',
                    EXTENSION,
                    for_=IPloneSiteRoot)

from config import GLOBALS
registerDirectory('skins', GLOBALS)

def initialize(context):
    pass

    #import patches
    #patches.run()

