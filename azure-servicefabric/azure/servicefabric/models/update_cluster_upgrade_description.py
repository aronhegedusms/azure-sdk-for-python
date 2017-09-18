# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateClusterUpgradeDescription(Model):
    """Parameters for updating a cluster upgrade.

    :param upgrade_kind: Possible values include: 'Invalid', 'Rolling',
     'Rolling_ForceRestart'. Default value: "Rolling" .
    :type upgrade_kind: str
    :param update_description:
    :type update_description: :class:`RollingUpgradeUpdateDescription
     <azure.servicefabric.models.RollingUpgradeUpdateDescription>`
    :param cluster_health_policy:
    :type cluster_health_policy: :class:`ClusterHealthPolicy
     <azure.servicefabric.models.ClusterHealthPolicy>`
    :param enable_delta_health_evaluation:
    :type enable_delta_health_evaluation: bool
    :param cluster_upgrade_health_policy:
    :type cluster_upgrade_health_policy:
     :class:`ClusterUpgradeHealthPolicyObject
     <azure.servicefabric.models.ClusterUpgradeHealthPolicyObject>`
    :param application_health_policy_map:
    :type application_health_policy_map: :class:`ApplicationHealthPolicies
     <azure.servicefabric.models.ApplicationHealthPolicies>`
    """ 

    _attribute_map = {
        'upgrade_kind': {'key': 'UpgradeKind', 'type': 'str'},
        'update_description': {'key': 'UpdateDescription', 'type': 'RollingUpgradeUpdateDescription'},
        'cluster_health_policy': {'key': 'ClusterHealthPolicy', 'type': 'ClusterHealthPolicy'},
        'enable_delta_health_evaluation': {'key': 'EnableDeltaHealthEvaluation', 'type': 'bool'},
        'cluster_upgrade_health_policy': {'key': 'ClusterUpgradeHealthPolicy', 'type': 'ClusterUpgradeHealthPolicyObject'},
        'application_health_policy_map': {'key': 'ApplicationHealthPolicyMap', 'type': 'ApplicationHealthPolicies'},
    }

    def __init__(self, upgrade_kind="Rolling", update_description=None, cluster_health_policy=None, enable_delta_health_evaluation=None, cluster_upgrade_health_policy=None, application_health_policy_map=None):
        self.upgrade_kind = upgrade_kind
        self.update_description = update_description
        self.cluster_health_policy = cluster_health_policy
        self.enable_delta_health_evaluation = enable_delta_health_evaluation
        self.cluster_upgrade_health_policy = cluster_upgrade_health_policy
        self.application_health_policy_map = application_health_policy_map
