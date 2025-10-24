# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import collective.smartlink


class CollectiveSmartlinkLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.smartlink)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.smartlink:default")


COLLECTIVE_SMARTLINK_FIXTURE = CollectiveSmartlinkLayer()


COLLECTIVE_SMARTLINK_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SMARTLINK_FIXTURE,),
    name="CollectiveSmartlinkLayer:IntegrationTesting",
)


COLLECTIVE_SMARTLINK_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SMARTLINK_FIXTURE,),
    name="CollectiveSmartlinkLayer:FunctionalTesting",
)
