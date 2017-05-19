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
from plone.directives import form
from z3c.relationfield.schema import RelationChoice
from plone.app.contenttypes.interfaces import ILink
from plone.app.z3cform.widget import RelatedItemsFieldWidget


@provider(IFormFieldProvider)
class ISmartLinkExtension(model.Schema):

    # form.widget(internal_link=ContentTreeFieldWidget)
    internal_link = RelationChoice(
        title=_(u'label_smartlink_internallink', default='Internal link'),
        description=_(u'help_smartlink_internallink',
                        default=u"Browse to find the internal page to which you wish to link. "
                        u"If this field is used, then any entry in the external link field will be ignored. "
                        u"You cannot have both an internal and external link."),
        required=False,
        vocabulary='plone.app.vocabularies.Catalog'
    )
    form.widget(
        'internal_link',
        RelatedItemsFieldWidget,
        vocabulary='plone.app.vocabularies.Catalog'
    )


class ISmartLinkMarker(ILink):
    """ """


@implementer(ISmartLinkExtension)
@adapter(IDexterityContent)
class SmartLinkExtension(object):

    def __init__(self, context):
        self.context = context
