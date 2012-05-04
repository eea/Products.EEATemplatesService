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
        if jsdisable == 'all':
            tree = lxml.html.fromstring(requiredhead)
            head = tree.findall('head')[0]
            for script in head.findall('script'):
                head.remove(script)

            kss_links = ['kss-base-url', 'kinetic-stylesheet']
            for link in head.findall('link'):
                for link_value in link.values():
                    if link_value in kss_links:
                        head.remove(link)
                        break

            requiredhead = lxml.html.tostring(tree)

        return requiredhead

    def getHeader(self):
        """return head template"""
        site = getattr(self.request, 'site', 'NotProvided')
        tabselected = getattr(self.request, 'tabselected', 'dummyselectedid')
        jsdisable = getattr(self.request, 'jsdisable', '')
        self.context.REQUEST.set('jsdisable', jsdisable)
        if site == 'NotProvided':
            site = getattr(self.context, 'navigationmanager_site', 'default')
        return self.context.eea_header(
                                site=site,
                                tabselected=tabselected,
                                jsdisable=jsdisable)


    def getFooter(self):
        """return head template"""
        return self.context.eea_footer()

