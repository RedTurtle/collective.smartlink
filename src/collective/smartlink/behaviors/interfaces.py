# -*- coding: utf-8 -*-
from .. import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider

from plone.namedfile.field import NamedBlobImage
from collective.smartlink.interfaces import ICollectiveSmartLink

from .. import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from plone.formwidget.contenttree import MultiContentTreeFieldWidget
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.interface import alsoProvides
from plone.supermodel.interfaces import FIELDSETS_KEY
from plone.supermodel.model import Fieldset

from plone.app.contenttypes.interfaces import IDocument
from plone.app.vocabularies.catalog import CatalogSource


@provider(IFormFieldProvider)
class ISmartLinkExtension(model.Schema):

    # form.widget(internal_link=ContentTreeFieldWidget)
    # internal_link = RelationChoice(
    #         title=u"Related",
    #         source=ObjPathSourceBinder(),
    #     ),

    # form.widget(related_office=MultiContentTreeFieldWidget)
    #
    # related_office = RelationList(
    #     title=_(u'label_related_office', default=u'Related office'),
    #     default=[],
    #     value_type=RelationChoice(
    #         title=u"Related",
    #         source=ObjPathSourceBinder(
    #             ),
    #     ),
    #     required=False
    # )

    internal_link = schema.TextLine(
        title=_(u'label_smartlink_internallink', default='Internal link'),
        required = False,
        description=_(u'help_smartlink_internallink',
                        default=u"Browse to find the internal page to which you wish to link. "
                                u"If this field is used, then any entry in the external link field will be ignored. "
                                u"You cannot have both an internal and external link."),
    )

    favicon = NamedBlobImage(
        title=_(u'label_smartlink_favicon', default=u'Icon'),
        required=False,
        description=_(u'help_smartlink_favicon',
                        default=(u'You can customize there the content icon. '
                                 u'You can use this for provide the icon of the remote site')),
    )


@implementer(ISmartLinkExtension)
@adapter(IDexterityContent)
class SmartLinkExtension(object):

    def __init__(self, context):
        self.context = context

    # def getIcon(self, relative_to_portal=0):
    #     """If a favicon was provided, show it"""
    #     import pdb; pdb.set_trace()
        # if not self.getFavicon():
        #     return ATLink.getIcon(self, relative_to_portal)
        #
        # utool = getToolByName(self, 'portal_url')
        # if relative_to_portal:
        #     return self.absolute_url().replace(utool()+'/',"") + '/favicon'
        # # Relative to REQUEST['BASEPATH1']
        # res = utool(relative=1) + self.absolute_url().replace(utool(),"") + '/favicon'
        # while res[:1] == '/':
        #     res = res[1:]
        # return res
