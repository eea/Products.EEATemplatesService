""" Base test module
"""
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.GenericSetup import EXTENSION, profile_registry
from Products.CMFPlone.interfaces import IPloneSiteRoot
import Products.EEATemplateService

@onsetup
def setup_eeacontenttypes():
    """ Setup eeacontenttypes
    """
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', Products.EEATemplateService)
    fiveconfigure.debug_mode = False

    PloneTestCase.installPackage('collective.monkeypatcher')
    PloneTestCase.installPackage('collective.fastview')

setup_eeacontenttypes()
PloneTestCase.setupPloneSite(extension_profiles=(
    'Products.EEATemplatesService:default',
    'Products.EEATemplatesService:testfixture'))

class EEATemplatesService(PloneTestCase.FunctionalTestCase):
    """ EEATemplatesService FunctionalTestCase class
    """
