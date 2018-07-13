# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.green


class PlonethemeGreenLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.green)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.green:default')


PLONETHEME_GREEN_FIXTURE = PlonethemeGreenLayer()


PLONETHEME_GREEN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_GREEN_FIXTURE,),
    name='PlonethemeGreenLayer:IntegrationTesting'
)


PLONETHEME_GREEN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_GREEN_FIXTURE,),
    name='PlonethemeGreenLayer:FunctionalTesting'
)


PLONETHEME_GREEN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_GREEN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeGreenLayer:AcceptanceTesting'
)
