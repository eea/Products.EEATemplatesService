=====================
EEA Template Services
=====================
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/Products.EEATemplatesService/develop
  :target: https://ci.eionet.europa.eu/job/eea/job/Products.EEATemplatesService/job/develop/display/redirect
  :alt: Develop
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/Products.EEATemplatesService/master
  :target: https://ci.eionet.europa.eu/job/eea/job/Products.EEATemplatesService/job/master/display/redirect
  :alt: Master

EEATemplatesService is a product that provieds simple HTTP service for the
templates from the plone site.

The template service will be able to deploy templates elements on-the-fly
by simple HTTP requests. There is no need to use a more advanced technique
like SOAP or XML-RPC at this stage.

getRequiredHead
getHeader
getFooter
getBaseBreadcrumb

EEATemplatesService is based on DIYPloneStyle 1.0.4, a skeleton product
ready for building new graphical designs for Plone.


Contents
========

.. contents::


Installation
============

Place EEATemplatesService in the Products directory of your Zope instance
and restart the server.

In Plone go to the 'Site Setup' page and click on the 'Add/Remove
Products' link.

Choose EEATemplatesService (check its checkbox) and click the 'Install' button.

You may have to empty your browser cache to see the effects of the
product installation/uninstallation.

Uninstall -- This can be done from the same management screen.

Selecting a skin
----------------

Depending on the value given to SELECTSKIN (in config.py), the skin will be
selected (or not) as default one while installing the product. If you need
to switch from a default skin to another, go to the 'Site Setup' page, and
choose 'Skins' (as portal manager). You can also decide from that page if
members can choose their preferred skin and, in that case, if the skin
cookie should be persistent.

Note -- Don't forget to perform a full refresh of the page or reload all
images (not from browser cache) after selecting a skin.
In Firefox, you can do so by pressing the 'shift' key while reloading the
page. In IE, use the key combination <Ctrl-F5>.

Source code
===========

- Latest source code (Plone 4 compatible):
  https://github.com/eea/Products.EEATemplatesService


Copyright and license
=====================
The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Templates Service (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

More details under docs/License.txt


Funding
=======

EEA_ - European Environment Agency (EU)

.. _EEA: https://www.eea.europa.eu/
