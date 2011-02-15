""" setup.py """

from setuptools import setup, find_packages
import os

name = 'Products.EEATemplatesService'
path = name.split('.') + ['version.txt']
version = open(os.path.join(*path)).read().strip()

setup(
 name='Products.EEATemplatesService',
 version=version,
 description="EEATemplatesService is a products that provides simple http \
         services for the templates of a plone site",
 long_description=open("README.txt").read() + "\n" +
                  open(os.path.join("docs", "HISTORY.txt")).read(),
 url="https://svn.eionet.europa.eu/projects/"
     "Zope/browser/trunk/Products.EEATemplatesService",
 classifiers=[
   "Framework :: Plone",
   "Programming Language :: Python",
   ],
 keywords='EEATemplatesService',
 author='Sasha Vincic (EEA), European Environment Agency',
 author_email='webadmin@eea.europa.eu',
 license='GPL',
 packages=find_packages(exclude=['ez_setup']),
 namespace_packages=['Products'],
 include_package_data=True,
 zip_safe=False,
 install_requires=[
     "setuptools",
 ],
 entry_points="""
 # -*- Entry points: -*-
 """,
 )

