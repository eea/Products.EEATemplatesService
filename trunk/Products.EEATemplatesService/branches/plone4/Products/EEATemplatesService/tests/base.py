""" Base test module
"""
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.GenericSetup import EXTENSION, profile_registry
from Products.CMFPlone.interfaces import IPloneSiteRoot

PRODUCTS = ['CacheSetup', 'collective.monkeypatcher',  'EEATemplatesService']

profile_registry.registerProfile(
                    'testfixture',
                    'EEATemplatesService',
                    'Extension profile with EEA workflows and content types',
                    'profiles/testfixture',
                    'EEATemplatesService',
                    EXTENSION,
                    for_=IPloneSiteRoot)



@onsetup
def setup_eeacontenttypes():
    """ setup_eeacontenttypes test setup function """
    fiveconfigure.debug_mode = True
    import Products.Five
    import collective.monkeypatcher
    import Products.CMFSquidTool
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('meta.zcml', collective.monkeypatcher)
    zcml.load_config('configure.zcml', Products.CMFSquidTool)
    PloneTestCase.installProduct('Five')
    PloneTestCase.installProduct('colective.monkeypatcher')
    PloneTestCase.installProduct('CMFSquidTool')
    fiveconfigure.debug_mode = False

    for product in PRODUCTS:
        PloneTestCase.installProduct(product)


setup_eeacontenttypes()
PloneTestCase.setupPloneSite(extension_profiles=['Products.EEATemplatesService:default',
  'Products.EEATemplatesService:testfixture'   ], products=PRODUCTS)

class EEATemplatesService(PloneTestCase.FunctionalTestCase):
    """ EEATemplatesService FunctionalTestCase class """
