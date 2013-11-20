"""external templates"""
import lxml

class ExternalTemplates(object):
    """external templates"""
    def getRequiredHead(self):
        """return required head template"""
        jsdisable = getattr(self.request, 'jsdisable', '')
        self.context.REQUEST.set('jsdisable', jsdisable)
        requiredhead = self.context.eea_requiredhead(jsdisable=jsdisable)

        return requiredhead

    def getHeader(self):
        """return head template"""
        jsdisable = getattr(self.request, 'jsdisable', '')
        self.context.REQUEST.set('jsdisable', jsdisable)

        header = self.context.eea_header(jsdisable=jsdisable)

        tree = lxml.html.fromstring(header)
        tree.make_links_absolute(self.context.absolute_url())
        #remove the plone login which should never be used by external systems.
        elementIdsToRemove = ['portal-personaltools-wrapper',
                                'siteaction-login']
        for elementId in elementIdsToRemove:
            # pass a string default parameter otherwise if element is not
            # found it will return a keyError
            element = tree.get_element_by_id(elementId, '')
            if element:
                element.getparent().remove(element)

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

