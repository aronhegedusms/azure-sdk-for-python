# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class DeviceLocationVerificationContent(_model_base.Model):
    """Request to verify Location.

    All required parameters must be populated in order to send to server.

    :ivar network_identifier: Network to query for this device, or device information to enable
     network routing. Required.
    :vartype network_identifier: ~azure.programmableconnectivity.models.NetworkIdentifier
    :ivar latitude: Latitude of location to be verified. Required.
    :vartype latitude: float
    :ivar longitude: Longitude of location to be verified. Required.
    :vartype longitude: float
    :ivar accuracy: Accuracy expected for location verification in kilometers. Required.
    :vartype accuracy: int
    :ivar device: The device to find the location for. Exactly one of Network Access Code, Phone
     Number, IPv4 address, or IPv6 address. Required.
    :vartype device: ~azure.programmableconnectivity.models.LocationDevice
    """

    network_identifier: "_models.NetworkIdentifier" = rest_field(name="networkIdentifier")
    """Network to query for this device, or device information to enable network routing. Required."""
    latitude: float = rest_field()
    """Latitude of location to be verified. Required."""
    longitude: float = rest_field()
    """Longitude of location to be verified. Required."""
    accuracy: int = rest_field()
    """Accuracy expected for location verification in kilometers. Required."""
    device: "_models.LocationDevice" = rest_field()
    """The device to find the location for. Exactly one of Network Access Code, Phone Number, IPv4
     address, or IPv6 address. Required."""

    @overload
    def __init__(
        self,
        *,
        network_identifier: "_models.NetworkIdentifier",
        latitude: float,
        longitude: float,
        accuracy: int,
        device: "_models.LocationDevice",
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DeviceLocationVerificationResult(_model_base.Model):
    """Response verifying location.

    All required parameters must be populated in order to send to server.

    :ivar verification_result: True if the location is in the specified area, False otherwise.
     Required.
    :vartype verification_result: bool
    """

    verification_result: bool = rest_field(name="verificationResult")
    """True if the location is in the specified area, False otherwise. Required."""

    @overload
    def __init__(
        self,
        *,
        verification_result: bool,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Ipv4Address(_model_base.Model):
    """IPv4 device indicator.

    All required parameters must be populated in order to send to server.

    :ivar ipv4: An IPv4 address. This may be specified as an exact address, or as a subnet in CIDR
     notation. Required.
    :vartype ipv4: str
    :ivar port: User equipment port. Required.
    :vartype port: int
    """

    ipv4: str = rest_field()
    """An IPv4 address. This may be specified as an exact address, or as a subnet in CIDR notation.
     Required."""
    port: int = rest_field()
    """User equipment port. Required."""

    @overload
    def __init__(
        self,
        *,
        ipv4: str,
        port: int,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Ipv6Address(_model_base.Model):
    """IPv6 device indicator.

    All required parameters must be populated in order to send to server.

    :ivar ipv6: An IPv6 address. This may be specified as an exact address, or as a subnet in CIDR
     notation. Required.
    :vartype ipv6: str
    :ivar port: User equipment port. Required.
    :vartype port: int
    """

    ipv6: str = rest_field()
    """An IPv6 address. This may be specified as an exact address, or as a subnet in CIDR notation.
     Required."""
    port: int = rest_field()
    """User equipment port. Required."""

    @overload
    def __init__(
        self,
        *,
        ipv6: str,
        port: int,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class LocationDevice(_model_base.Model):
    """Device information needed by operator to provide location information. Include exactly one of
    these properties to identify your device.

    :ivar network_access_identifier: External identifier or network access identifier of the
     device.
    :vartype network_access_identifier: str
    :ivar phone_number: Phone number in E.164 format (starting with country code), and optionally
     prefixed with '+'.
    :vartype phone_number: str
    :ivar ipv4_address: The Ipv4 address.
    :vartype ipv4_address: ~azure.programmableconnectivity.models.Ipv4Address
    :ivar ipv6_address: The Ipv6 address.
    :vartype ipv6_address: ~azure.programmableconnectivity.models.Ipv6Address
    """

    network_access_identifier: Optional[str] = rest_field(name="networkAccessIdentifier")
    """External identifier or network access identifier of the device."""
    phone_number: Optional[str] = rest_field(name="phoneNumber")
    """Phone number in E.164 format (starting with country code), and optionally prefixed with '+'."""
    ipv4_address: Optional["_models.Ipv4Address"] = rest_field(name="ipv4Address")
    """The Ipv4 address."""
    ipv6_address: Optional["_models.Ipv6Address"] = rest_field(name="ipv6Address")
    """The Ipv6 address."""

    @overload
    def __init__(
        self,
        *,
        network_access_identifier: Optional[str] = None,
        phone_number: Optional[str] = None,
        ipv4_address: Optional["_models.Ipv4Address"] = None,
        ipv6_address: Optional["_models.Ipv6Address"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class NetworkIdentifier(_model_base.Model):
    """Identifier for the network to be queried.

    All required parameters must be populated in order to send to server.

    :ivar identifier_type: The type of identifier for the network. one of: 'IPv4', 'IPv6',
     'NetworkCode'. Required.
    :vartype identifier_type: str
    :ivar identifier: The network identifier, based on the identifierType: an IPv4 address, and
     IPv6 address, or a Network Code.
     A Network Code may be obtained from APC documentation or from the APC /Network:retrieve
     endpoint. Required.
    :vartype identifier: str
    """

    identifier_type: str = rest_field(name="identifierType")
    """The type of identifier for the network. one of: 'IPv4', 'IPv6', 'NetworkCode'. Required."""
    identifier: str = rest_field()
    """The network identifier, based on the identifierType: an IPv4 address, and IPv6 address, or a
     Network Code.
     A Network Code may be obtained from APC documentation or from the APC /Network:retrieve
     endpoint. Required."""

    @overload
    def __init__(
        self,
        *,
        identifier_type: str,
        identifier: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class NetworkRetrievalResult(_model_base.Model):
    """The network that the device is on.

    All required parameters must be populated in order to send to server.

    :ivar network_code: The identifier for the network. This can be used as the networkIdentifier
     for the service APIs. Required.
    :vartype network_code: str
    """

    network_code: str = rest_field(name="networkCode")
    """The identifier for the network. This can be used as the networkIdentifier for the service APIs.
     Required."""

    @overload
    def __init__(
        self,
        *,
        network_code: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class NumberVerificationResult(_model_base.Model):
    """Response verifying number of device.

    All required parameters must be populated in order to send to server.

    :ivar verification_result: True if number if the phone number matches the device, False
     otherwise. Required.
    :vartype verification_result: bool
    """

    verification_result: bool = rest_field(name="verificationResult")
    """True if number if the phone number matches the device, False otherwise. Required."""

    @overload
    def __init__(
        self,
        *,
        verification_result: bool,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class NumberVerificationWithCodeContent(_model_base.Model):
    """Request to verify number of device - second call.

    All required parameters must be populated in order to send to server.

    :ivar apc_code: The code provided by APC in exchange for the operator code. Required.
    :vartype apc_code: str
    """

    apc_code: str = rest_field(name="apcCode")
    """The code provided by APC in exchange for the operator code. Required."""

    @overload
    def __init__(
        self,
        *,
        apc_code: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class NumberVerificationWithoutCodeContent(_model_base.Model):
    """Request to verify number of device - first call.

    All required parameters must be populated in order to send to server.

    :ivar network_identifier: Identifier for the network to query for this device. Required.
    :vartype network_identifier: ~azure.programmableconnectivity.models.NetworkIdentifier
    :ivar phone_number: Phone number in E.164 format (starting with country code), and optionally
     prefixed with '+'.
    :vartype phone_number: str
    :ivar hashed_phone_number: Hashed phone number. SHA-256 (in hexadecimal representation) of the
     mobile phone number in **E.164 format (starting with country code)**. Optionally prefixed with
     '+'.
    :vartype hashed_phone_number: str
    :ivar redirect_uri: Redirect URI to backend application. Required.
    :vartype redirect_uri: str
    """

    network_identifier: "_models.NetworkIdentifier" = rest_field(name="networkIdentifier")
    """Identifier for the network to query for this device. Required."""
    phone_number: Optional[str] = rest_field(name="phoneNumber")
    """Phone number in E.164 format (starting with country code), and optionally prefixed with '+'."""
    hashed_phone_number: Optional[str] = rest_field(name="hashedPhoneNumber")
    """Hashed phone number. SHA-256 (in hexadecimal representation) of the mobile phone number in
     **E.164 format (starting with country code)**. Optionally prefixed with '+'."""
    redirect_uri: str = rest_field(name="redirectUri")
    """Redirect URI to backend application. Required."""

    @overload
    def __init__(
        self,
        *,
        network_identifier: "_models.NetworkIdentifier",
        redirect_uri: str,
        phone_number: Optional[str] = None,
        hashed_phone_number: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class SimSwapRetrievalContent(_model_base.Model):
    """Request to retrieve SimSwap date.

    All required parameters must be populated in order to send to server.

    :ivar phone_number: Phone number in E.164 format (starting with country code), and optionally
     prefixed with '+'.
    :vartype phone_number: str
    :ivar network_identifier: Network to query for this device. Required.
    :vartype network_identifier: ~azure.programmableconnectivity.models.NetworkIdentifier
    """

    phone_number: Optional[str] = rest_field(name="phoneNumber")
    """Phone number in E.164 format (starting with country code), and optionally prefixed with '+'."""
    network_identifier: "_models.NetworkIdentifier" = rest_field(name="networkIdentifier")
    """Network to query for this device. Required."""

    @overload
    def __init__(
        self,
        *,
        network_identifier: "_models.NetworkIdentifier",
        phone_number: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class SimSwapRetrievalResult(_model_base.Model):
    """Response with SimSwap date.

    :ivar date: Datetime of most recent swap for SIM.
    :vartype date: ~datetime.datetime
    """

    date: Optional[datetime.datetime] = rest_field(format="rfc3339")
    """Datetime of most recent swap for SIM."""

    @overload
    def __init__(
        self,
        *,
        date: Optional[datetime.datetime] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class SimSwapVerificationContent(_model_base.Model):
    """Request to verify SimSwap in period.

    All required parameters must be populated in order to send to server.

    :ivar phone_number: Phone number in E.164 format (starting with country code), and optionally
     prefixed with '+'.
    :vartype phone_number: str
    :ivar max_age_hours: Maximum lookback for SimSwap verification.
    :vartype max_age_hours: int
    :ivar network_identifier: Identifier for the network to query for this device. Required.
    :vartype network_identifier: ~azure.programmableconnectivity.models.NetworkIdentifier
    """

    phone_number: Optional[str] = rest_field(name="phoneNumber")
    """Phone number in E.164 format (starting with country code), and optionally prefixed with '+'."""
    max_age_hours: Optional[int] = rest_field(name="maxAgeHours")
    """Maximum lookback for SimSwap verification."""
    network_identifier: "_models.NetworkIdentifier" = rest_field(name="networkIdentifier")
    """Identifier for the network to query for this device. Required."""

    @overload
    def __init__(
        self,
        *,
        network_identifier: "_models.NetworkIdentifier",
        phone_number: Optional[str] = None,
        max_age_hours: Optional[int] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class SimSwapVerificationResult(_model_base.Model):
    """Response verifying SimSwap in period.

    All required parameters must be populated in order to send to server.

    :ivar verification_result: True if the SIM has swapped in the specified period, False
     otherwise. Required.
    :vartype verification_result: bool
    """

    verification_result: bool = rest_field(name="verificationResult")
    """True if the SIM has swapped in the specified period, False otherwise. Required."""

    @overload
    def __init__(
        self,
        *,
        verification_result: bool,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
