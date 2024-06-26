# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------


def _format_url_section(template, **kwargs):
    components = template.split("/")
    while components:
        try:
            return template.format(**kwargs)
        except KeyError as key:
            formatted_components = template.split("/")
            components = [c for c in formatted_components if "{}".format(key.args[0]) not in c]
            template = "/".join(components)


def raise_if_not_implemented(cls, abstract_methods):
    not_implemented = [f for f in abstract_methods if not callable(getattr(cls, f, None))]
    if not_implemented:
        raise NotImplementedError(
            "The following methods on operation group '{}' are not implemented: '{}'."
            " Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.".format(
                cls.__name__, "', '".join(not_implemented)
            )
        )
