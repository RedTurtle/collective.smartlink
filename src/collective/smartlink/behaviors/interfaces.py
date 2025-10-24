# -*- coding: utf-8 -*-
from collective.smartlink import _  # noqa
from plone.app.contenttypes.interfaces import ILink  # noqa
from plone.app.z3cform.widget import RelatedItemsFieldWidget  # noqa
from plone.autoform import directives  # noqa
from plone.autoform.interfaces import IFormFieldProvider  # noqa
from plone.dexterity.interfaces import IDexterityContent  # noqa
from plone.namedfile.field import NamedBlobImage  # noqa
from plone.supermodel import model  # noqa
from z3c.relationfield.schema import RelationChoice  # noqa
from zope import schema  # noqa
from zope.component import adapter  # noqa
from zope.interface import implementer  # noqa
from zope.interface import Interface
from zope.interface import provider  # noqa


class ISmartLinkExtension(Interface):
    """Marker interface for Links."""
