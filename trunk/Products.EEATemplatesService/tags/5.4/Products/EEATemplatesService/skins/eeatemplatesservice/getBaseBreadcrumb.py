## Script (Python) "getBaseBreadcrumb"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=site='default',menuid=''
##title=Returns base breadcrumbs

return context.eea_basebreadcrumb(site=site,menuid=menuid)