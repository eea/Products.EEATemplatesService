import lxml

class ExternalTemplates(object):
    """external templates"""
    def getRequiredHead(self):
        """required head"""
        jsdisable = getattr(self.request,'jsdisable','')
        portal_properties = { 'title' : 'Portal title' }
        self.context.REQUEST.set('jsdisable',jsdisable)
        requiredhead = self.context.eea_requiredhead(
                                portal_properties=portal_properties,
                                jsdisable=jsdisable)
        if jsdisable == 'all':
            tree = lxml.html.fromstring(requiredhead)
            head = tree.findall('head')[0]
            for script in head.findall('script'):
                head.remove(script)

            kss_links = ['kss-base-url', 'kinetic-stylesheet'];
            for link in head.findall('link'):
                for link_value in link.values():
                    if link_value in kss_links:
                        head.remove(link)
                        break

            requiredhead = lxml.html.tostring(tree)
        return requiredhead
