## Script (Python) "getRequiredHead"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=site='default',jsdisable=''
##title=Returns required head for the websited

portal_properties = { 'title' : 'Portal title' }
context.REQUEST.set('jsdisable',jsdisable)
return context.eea_requiredhead(portal_properties=portal_properties, jsdisable=jsdisable)
