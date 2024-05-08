# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import ApplicationClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python delete_application_definition.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ApplicationClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    client.application_definitions.begin_delete_by_id(
        resource_group_name="rg",
        application_definition_name="myManagedApplicationDef",
    ).result()


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Solutions/stable/2019-07-01/examples/deleteApplicationDefinition.json
if __name__ == "__main__":
    main()
