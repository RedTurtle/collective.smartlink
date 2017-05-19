# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
from plone.app.contenttypes.utils import replace_link_variables_by_paths
from collective.smartlink.behaviors.interfaces import ISmartLinkMarker


@indexer(ISmartLinkMarker)
def getRemoteUrl(obj):
    url = obj.internal_link or obj.remoteUrl
    return replace_link_variables_by_paths(obj, url)
