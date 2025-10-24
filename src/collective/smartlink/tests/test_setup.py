# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.smartlink.testing import (  # noqa
    COLLECTIVE_SMARTLINK_INTEGRATION_TESTING,
)
from plone import api

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.smartlink is properly installed."""

    layer = COLLECTIVE_SMARTLINK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.smartlink is installed."""
        self.assertTrue(self.installer.is_product_installed("collective.smartlink"))

    def test_browserlayer(self):
        """Test that ICollectiveSmartlinkLayer is registered."""
        from collective.smartlink.interfaces import ICollectiveSmartlinkLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveSmartlinkLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_SMARTLINK_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        self.installer.uninstall_product("collective.smartlink")

    def test_product_uninstalled(self):
        """Test if collective.smartlink is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("collective.smartlink"))

    def test_browserlayer_removed(self):
        """Test that ICollectiveSmartlinkLayer is removed."""
        from collective.smartlink.interfaces import ICollectiveSmartlinkLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveSmartlinkLayer, utils.registered_layers())
