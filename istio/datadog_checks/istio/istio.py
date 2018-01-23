# (C) Datadog, Inc. 2010-2018
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

# stdlib
import re
import traceback
from contextlib import closing, contextmanager
from collections import defaultdict

# 3p

# project
from config import _is_affirmative
from checks import AgentCheck

from . import envoy, mesh, mixer


class Istio(AgentCheck):

    def __init__(self, name, init_config, agentConfig, instances=None):
        super(Istio, self).__init__(name, init_config, agentConfig, instances)

        # Instead of one check, use three
        self.mesh_check = mesh.IstioMeshCheck(name, init_config, agentConfig, instances)
        self.mixer_check = mixer.MixerCheck(name, init_config, agentConfig, instances)
        self.envoy_check = envoy.IstioEnvoyCheck(name, init_config, agentConfig, instances)

        # Make sure they all have the same aggregator so that the status page works
        self.mesh_check.aggregator = self.aggregator
        self.mixer_check.aggregator = self.aggregator
        self.envoy_check.aggregator = self.aggregator


    def check(self, instance):
        self.log.debug('running all istio checks')

        # run the checks
        self.mesh_check.check(instance)
        self.mixer_check.check(instance)
        self.envoy_check.check(instance)
