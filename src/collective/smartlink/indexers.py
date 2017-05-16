# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
from plone.app.contenttypes.utils import replace_link_variables_by_paths
from plone.dexterity.interfaces import IDexterityContent
from collective.smartlink.behaviors.interfaces import ISmartLinkMarker
from zope.schema import getFieldsInOrder
from plone.behavior.interfaces import IBehaviorAssignable


from Acquisition import aq_inner
from plone.memoize.view import memoize
from Products.Five import BrowserView
from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.interfaces import referenceable


@indexer(ISmartLinkMarker)
def getRemoteUrl(obj):    
    url = obj.internal_link or obj.remoteUrl
    return replace_link_variables_by_paths(obj, url)


@indexer(IDexterityContent)
def getIcon(obj):
    """
    geticon redefined in Plone > 5.0
    see https://github.com/plone/Products.CMFPlone/issues/1226
    reuse of metadata field,
    now used for showing thumbs in content listings etc.
    when obj is an image or has a lead image
    or has an image field with name 'image': true else false
    """
    if obj.aq_base.image:
        return True
    return False
