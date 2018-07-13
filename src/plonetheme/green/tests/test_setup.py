# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plonetheme.green.testing import PLONETHEME_GREEN_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.green is properly installed."""

    layer = PLONETHEME_GREEN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.green is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.green'))

    def test_browserlayer(self):
        """Test that IPlonethemeGreenLayer is registered."""
        from plonetheme.green.interfaces import (
            IPlonethemeGreenLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeGreenLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_GREEN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plonetheme.green'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plonetheme.green is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.green'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeGreenLayer is removed."""
        from plonetheme.green.interfaces import \
            IPlonethemeGreenLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPlonethemeGreenLayer,
            utils.registered_layers(),
        )
