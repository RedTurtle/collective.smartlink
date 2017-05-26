# -*- coding: utf-8 -*-
from plone.app.contenttypes.browser.link_redirect_view import LinkRedirectView as Base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LinkRedirectView(Base):
    index = ViewPageTemplateFile('templates/link.pt')

    def absolute_target_url(self):
        """Compute the absolute target URL."""
        if self.context.internal_link:
            return self.context.internal_link.to_object.absolute_url()
        else:
            return super(LinkRedirectView, self).absolute_target_url()
