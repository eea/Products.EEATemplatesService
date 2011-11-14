## Script (Python) "getHeader"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=site='NotProvided',tabselected='dummyselectedid'
##title=Returns header for the website

if site == 'NotProvided':
    site = getattr(context, 'navigationmanager_site', 'default')
    
return context.eea_header(site=site,tabselected=tabselected)
