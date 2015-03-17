""" Base test module
"""
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure
import Products.EEATemplatesService
    
@onsetup
def setup_eeacontenttypes():
    """ Setup eeacontenttypes
    """
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', Products.EEATemplatesService)
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
