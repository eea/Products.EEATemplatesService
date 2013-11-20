""" EEA Templates Service installer
"""
from setuptools import setup, find_packages
import os

NAME = 'Products.EEATemplatesService'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

setup(
    name=NAME,
    version=VERSION,
    description="EEA Templates Service is a products that provides simple "
                "http services for the templates of a plone site",
    long_description=open("README.txt").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    url="https://svn.eionet.europa.eu/projects/"
        "Zope/browser/trunk/Products.EEATemplatesService",
    classifiers=[
           "Framework :: Plone",
           "Programming Language :: Python",
           "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='EEA Templates Service',
    author='Sasha Vincic (EEA), European Environment Agency',
    author_email='webadmin@eea.europa.eu',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "collective.fastview",
        "collective.monkeypatcher",
        "lxml"
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
 )

