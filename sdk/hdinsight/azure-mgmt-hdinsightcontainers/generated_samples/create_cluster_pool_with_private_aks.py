# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.hdinsightcontainers import HDInsightContainersMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hdinsightcontainers
# USAGE
    python create_cluster_pool_with_private_aks.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HDInsightContainersMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="10e32bab-26da-4cc4-a441-52b318f824e6",
    )

    response = client.cluster_pools.begin_create_or_update(
        resource_group_name="hiloResourcegroup",
        cluster_pool_name="clusterpool1",
        cluster_pool={
            "location": "West US 2",
            "properties": {
                "clusterPoolProfile": {"clusterPoolVersion": "1.2"},
                "computeProfile": {"vmSize": "Standard_D3_v2"},
                "networkProfile": {
                    "enablePrivateApiServer": True,
                    "subnetId": "/subscriptions/subid/resourceGroups/hiloResourcegroup/providers/Microsoft.Network/virtualNetworks/vnet1/subnets/subnet1",
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsightOnAks/preview/2023-11-01-preview/examples/CreateClusterPoolWithPrivateAks.json
if __name__ == "__main__":
    main()
