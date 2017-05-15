# -*- coding: utf-8 -*-
from plone.app.contenttypes.interfaces import ILink
from plone.indexer.decorator import indexer
from plone.app.contenttypes.utils import replace_link_variables_by_paths
from plone.dexterity.interfaces import IDexterityContent

@indexer(ISmartLinkExtension)
def getRemoteUrl(obj):
    import pdb; pdb.set_trace()
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
