## Script (Python) "getSitemap"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=site='default',url=''
##title=Returns sub navigation for a specific site and url

return context.eea_sitemap(site=site)