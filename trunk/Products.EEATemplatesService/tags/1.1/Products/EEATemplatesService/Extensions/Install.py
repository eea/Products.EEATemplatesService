from cStringIO import StringIO

from Products.EEATemplatesService.Extensions.utils import *
from Products.EEATemplatesService.config import *

def install(self):
    out = StringIO()

    print >> out, "Installation completed."
    return out.getvalue()


def uninstall(self):
    out = StringIO()


