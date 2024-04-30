# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import ComputeManagementClientConfiguration
from .operations import (
    AvailabilitySetsOperations,
    CapacityReservationGroupsOperations,
    CapacityReservationsOperations,
    DedicatedHostGroupsOperations,
    DedicatedHostsOperations,
    ImagesOperations,
    LogAnalyticsOperations,
    Operations,
    ProximityPlacementGroupsOperations,
    RestorePointCollectionsOperations,
    RestorePointsOperations,
    SshPublicKeysOperations,
    UsageOperations,
    VirtualMachineExtensionImagesOperations,
    VirtualMachineExtensionsOperations,
    VirtualMachineImagesEdgeZoneOperations,
    VirtualMachineImagesOperations,
    VirtualMachineRunCommandsOperations,
    VirtualMachineScaleSetExtensionsOperations,
    VirtualMachineScaleSetRollingUpgradesOperations,
    VirtualMachineScaleSetVMExtensionsOperations,
    VirtualMachineScaleSetVMRunCommandsOperations,
    VirtualMachineScaleSetVMsOperations,
    VirtualMachineScaleSetsOperations,
    VirtualMachineSizesOperations,
    VirtualMachinesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class ComputeManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Compute Client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.compute.v2024_03_01.operations.Operations
    :ivar usage: UsageOperations operations
    :vartype usage: azure.mgmt.compute.v2024_03_01.operations.UsageOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineSizesOperations
    :ivar virtual_machine_scale_sets: VirtualMachineScaleSetsOperations operations
    :vartype virtual_machine_scale_sets:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineScaleSetsOperations
    :ivar virtual_machine_scale_set_extensions: VirtualMachineScaleSetExtensionsOperations
     operations
    :vartype virtual_machine_scale_set_extensions:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineScaleSetExtensionsOperations
    :ivar virtual_machine_scale_set_rolling_upgrades:
     VirtualMachineScaleSetRollingUpgradesOperations operations
    :vartype virtual_machine_scale_set_rolling_upgrades:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineScaleSetRollingUpgradesOperations
    :ivar virtual_machine_scale_set_vm_extensions: VirtualMachineScaleSetVMExtensionsOperations
     operations
    :vartype virtual_machine_scale_set_vm_extensions:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineScaleSetVMExtensionsOperations
    :ivar virtual_machine_scale_set_vms: VirtualMachineScaleSetVMsOperations operations
    :vartype virtual_machine_scale_set_vms:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineScaleSetVMsOperations
    :ivar virtual_machine_extensions: VirtualMachineExtensionsOperations operations
    :vartype virtual_machine_extensions:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineExtensionsOperations
    :ivar virtual_machines: VirtualMachinesOperations operations
    :vartype virtual_machines: azure.mgmt.compute.v2024_03_01.operations.VirtualMachinesOperations
    :ivar virtual_machine_images: VirtualMachineImagesOperations operations
    :vartype virtual_machine_images:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineImagesOperations
    :ivar virtual_machine_images_edge_zone: VirtualMachineImagesEdgeZoneOperations operations
    :vartype virtual_machine_images_edge_zone:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineImagesEdgeZoneOperations
    :ivar virtual_machine_extension_images: VirtualMachineExtensionImagesOperations operations
    :vartype virtual_machine_extension_images:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineExtensionImagesOperations
    :ivar availability_sets: AvailabilitySetsOperations operations
    :vartype availability_sets:
     azure.mgmt.compute.v2024_03_01.operations.AvailabilitySetsOperations
    :ivar proximity_placement_groups: ProximityPlacementGroupsOperations operations
    :vartype proximity_placement_groups:
     azure.mgmt.compute.v2024_03_01.operations.ProximityPlacementGroupsOperations
    :ivar dedicated_host_groups: DedicatedHostGroupsOperations operations
    :vartype dedicated_host_groups:
     azure.mgmt.compute.v2024_03_01.operations.DedicatedHostGroupsOperations
    :ivar dedicated_hosts: DedicatedHostsOperations operations
    :vartype dedicated_hosts: azure.mgmt.compute.v2024_03_01.operations.DedicatedHostsOperations
    :ivar ssh_public_keys: SshPublicKeysOperations operations
    :vartype ssh_public_keys: azure.mgmt.compute.v2024_03_01.operations.SshPublicKeysOperations
    :ivar images: ImagesOperations operations
    :vartype images: azure.mgmt.compute.v2024_03_01.operations.ImagesOperations
    :ivar restore_point_collections: RestorePointCollectionsOperations operations
    :vartype restore_point_collections:
     azure.mgmt.compute.v2024_03_01.operations.RestorePointCollectionsOperations
    :ivar restore_points: RestorePointsOperations operations
    :vartype restore_points: azure.mgmt.compute.v2024_03_01.operations.RestorePointsOperations
    :ivar capacity_reservation_groups: CapacityReservationGroupsOperations operations
    :vartype capacity_reservation_groups:
     azure.mgmt.compute.v2024_03_01.operations.CapacityReservationGroupsOperations
    :ivar capacity_reservations: CapacityReservationsOperations operations
    :vartype capacity_reservations:
     azure.mgmt.compute.v2024_03_01.operations.CapacityReservationsOperations
    :ivar log_analytics: LogAnalyticsOperations operations
    :vartype log_analytics: azure.mgmt.compute.v2024_03_01.operations.LogAnalyticsOperations
    :ivar virtual_machine_run_commands: VirtualMachineRunCommandsOperations operations
    :vartype virtual_machine_run_commands:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineRunCommandsOperations
    :ivar virtual_machine_scale_set_vm_run_commands: VirtualMachineScaleSetVMRunCommandsOperations
     operations
    :vartype virtual_machine_scale_set_vm_run_commands:
     azure.mgmt.compute.v2024_03_01.operations.VirtualMachineScaleSetVMRunCommandsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2024-03-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ComputeManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize, "2024-03-01")
        self.usage = UsageOperations(self._client, self._config, self._serialize, self._deserialize, "2024-03-01")
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_scale_sets = VirtualMachineScaleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_scale_set_extensions = VirtualMachineScaleSetExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_scale_set_rolling_upgrades = VirtualMachineScaleSetRollingUpgradesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_scale_set_vm_extensions = VirtualMachineScaleSetVMExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_scale_set_vms = VirtualMachineScaleSetVMsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_extensions = VirtualMachineExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machines = VirtualMachinesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_images = VirtualMachineImagesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_images_edge_zone = VirtualMachineImagesEdgeZoneOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_extension_images = VirtualMachineExtensionImagesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.availability_sets = AvailabilitySetsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.proximity_placement_groups = ProximityPlacementGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.dedicated_host_groups = DedicatedHostGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.dedicated_hosts = DedicatedHostsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.ssh_public_keys = SshPublicKeysOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.images = ImagesOperations(self._client, self._config, self._serialize, self._deserialize, "2024-03-01")
        self.restore_point_collections = RestorePointCollectionsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.restore_points = RestorePointsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.capacity_reservation_groups = CapacityReservationGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.capacity_reservations = CapacityReservationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.log_analytics = LogAnalyticsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_run_commands = VirtualMachineRunCommandsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )
        self.virtual_machine_scale_set_vm_run_commands = VirtualMachineScaleSetVMRunCommandsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2024-03-01"
        )

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ComputeManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
