## Script (Python) "getSubNavigation"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=site='default',menuid='',relativeurls='no',selectedsubmenuid='dummyselectedid'
##title=Returns sub navigation for a specific site and url

return context.eea_subnavigation(site=site,menuid=menuid,relativeurls=relativeurls,selectedsubmenuid=selectedsubmenuid)