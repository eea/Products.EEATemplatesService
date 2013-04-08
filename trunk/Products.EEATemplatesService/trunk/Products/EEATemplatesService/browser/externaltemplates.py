"""external templates"""
import lxml

class ExternalTemplates(object):
    """external templates"""
    def getRequiredHead(self):
        """return required head template"""
        jsdisable = getattr(self.request, 'jsdisable', '')
        portal_properties = { 'title' : 'Portal title' }
        self.context.REQUEST.set('jsdisable', jsdisable)
        requiredhead = self.context.eea_requiredhead(
                                portal_properties=portal_properties,
                                jsdisable=jsdisable)

        tree = lxml.html.fromstring(requiredhead)
        head = tree.findall('head')[0]
        for title in head.findall('title'):
            head.remove(title)

        if jsdisable == 'all':
            for script in head.findall('script'):
                head.remove(script)

            kss_links = ['kss-base-url', 'kinetic-stylesheet']
            for link in head.findall('link'):
                for link_value in link.values():
                    if link_value in kss_links:
                        head.remove(link)
                        break

        requiredhead = lxml.etree.tostring(tree)

        return requiredhead

    def getHeader(self):
        """return head template"""
        site = getattr(self.request, 'site', 'NotProvided')
        tabselected = getattr(self.request, 'tabselected', 'dummyselectedid')
        jsdisable = getattr(self.request, 'jsdisable', '')
        self.context.REQUEST.set('jsdisable', jsdisable)
        if site == 'NotProvided':
            site = getattr(self.context, 'navigationmanager_site', 'default')

        header = self.context.eea_header(
                                site=site,
                                tabselected=tabselected,
                                jsdisable=jsdisable)

        tree = lxml.html.fromstring(header)
        tree.make_links_absolute(self.context.absolute_url())
        #remove the plone login which should never be used by external systems.
        login_element = tree.get_element_by_id('portal-personaltools-wrapper')
        login_element.getparent().remove(login_element)
        return lxml.etree.tostring(tree)

    def getFooter(self):
        """return footer template"""
        footer = self.context.eea_footer()

        tree = lxml.html.fromstring(footer)
        links_to_remove = ['CMS login',
                            'Refresh this page',
                            'http://svn.eionet.europa.eu/projects/Zope/'+
                            'browser/trunk/www.eea.europa.eu/trunk/docs']
        links = {}
        iterator = tree.iter()
        while True:
            try:
                element = iterator.next()
                for obj_value in element.values():
                    if obj_value in links_to_remove:
                        ascensors = element.iterancestors()
                        parent = ascensors.next()
                        links[element] = parent
            except Exception:
                break
        for (k, v) in links.items():
            v.remove(k)
        return lxml.etree.tostring(tree)

