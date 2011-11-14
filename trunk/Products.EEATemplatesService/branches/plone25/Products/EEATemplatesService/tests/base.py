from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.GenericSetup import EXTENSION, profile_registry
from Products.CMFPlone.interfaces import IPloneSiteRoot

PRODUCTS = ['CacheSetup', 'EEATemplatesService']

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
    fiveconfigure.debug_mode = True
    import Products.Five
    import Products.CMFSquidTool
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.CMFSquidTool)    
    fiveconfigure.debug_mode = False

    PloneTestCase.installProduct('Five')
    PloneTestCase.installProduct('CMFSquidTool')
    for product in PRODUCTS:
        PloneTestCase.installProduct(product)


setup_eeacontenttypes()
PloneTestCase.setupPloneSite(extension_profiles=['EEATemplatesService:default', 'EEATemplatesService:testfixture'], products=PRODUCTS)

class EEATemplatesService(PloneTestCase.FunctionalTestCase):
    """ """
