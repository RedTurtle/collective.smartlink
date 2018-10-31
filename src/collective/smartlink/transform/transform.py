# -*- coding: utf-8 -*-
from App.config import getConfiguration
from lxml import etree
from os import environ
from plone.app.theming.interfaces import IThemingLayer
from plone.app.theming.utils import compileThemeTransform
from plone.app.theming.utils import findContext
from plone.app.theming.utils import getParser
from plone.app.theming.utils import prepareThemeParameters
from plone.app.theming.utils import theming_policy
from plone.app.theming.zmi import patch_zmi
from plone.transformchain.interfaces import ITransform
from repoze.xmliter.utils import getHTMLSerializer
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from collective.smartlink.interfaces import ICollectiveSmartlinkLayer


import logging


LOGGER = logging.getLogger('collective.smartlink.transform')


@implementer(ITransform)
@adapter(Interface, ICollectiveSmartlinkLayer)
class UidLinkTransform(object):
    """Late stage in the 8000's transform chain.
    When plone.app.blocks is used, we can benefit from lxml parsing having
    taken place already.
    """

    order = 8860

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def debug_theme(self):
        ''' Check if the theme should be debugged
        We will debug the theme
        when we have a truish diazo.debug parameter in the request
        '''
        if not getConfiguration().debug_mode:
            return False
        diazo_debug = self.request.get('diazo.debug', '').lower()
        return diazo_debug in ('1', 'y', 'yes', 't', 'true')

    def develop_theme(self):
        ''' Check if the theme should be recompiled
        every time the transform is applied
        '''
        if not getConfiguration().debug_mode:
            return False
        if self.debug_theme():
            return True
        if environ.get('DIAZO_ALWAYS_CACHE_RULES'):
            return False
        return True

    def setupTransform(self, runtrace=False):
        import pdb; pdb.set_trace()
        debug_mode = self.develop_theme()
        policy = theming_policy(self.request)

        # Obtain settings. Do nothing if not found
        settings = policy.getSettings()

        if settings is None:
            return None

        if not policy.isThemeEnabled():
            return None

        cache = policy.getCache()

        # Apply theme
        transform = None

        if not debug_mode:
            transform = cache.transform

        if transform is None:
            rules = settings.rules
            absolutePrefix = settings.absolutePrefix or None
            readNetwork = settings.readNetwork
            parameterExpressions = settings.parameterExpressions

            transform = compileThemeTransform(
                rules,
                absolutePrefix,
                readNetwork,
                parameterExpressions,
                runtrace=runtrace
            )
            if transform is None:
                return None

            if not debug_mode:
                cache.updateTransform(transform)

        return transform

    def getSettings(self):
        return theming_policy(self.request).getSettings()

    def parseTree(self, result):
        contentType = self.request.response.getHeader('Content-Type')
        if contentType is None or not contentType.startswith('text/html'):
            return None

        contentEncoding = self.request.response.getHeader('Content-Encoding')
        if contentEncoding \
           and contentEncoding in ('zip', 'deflate', 'compress',):
            return None

        try:
            return getHTMLSerializer(result, pretty_print=False)
        except (AttributeError, TypeError, etree.ParseError):
            return None

    def transformBytes(self, result, encoding):
        import pdb; pdb.set_trace()
        try:
            result = result.decode(encoding)
        except UnicodeDecodeError:
            # This is probably a file or an image
            # FIXME probably we do not event want to apply
            # this transform for files and images
            pass
        return self.transformIterable([result], encoding)

    def transformString(self, result, encoding):
        return self.transformIterable([result], encoding)

    def transformUnicode(self, result, encoding):
        return self.transformIterable([result], encoding)

    def transformIterable(self, result, encoding):
        """Apply the transform if required
        """
        import pdb; pdb.set_trace()

        return result
