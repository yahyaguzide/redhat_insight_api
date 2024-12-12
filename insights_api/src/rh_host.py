"""
Custom Host Object for Redhat Hosts data.
"""

from typing import Any
from dataclasses import dataclass, field


# class rh_vm_categories(Enum):
#    # Normal rhel category
#    #  RH028_26MO: int = 0  # 0=< x <9
#    #  RH028_27MO: int = 1  # 9=< x <128
#    #  RH028_28MO: int = 2  # 128>
#
#    RH028_26MO = 1
#    RH028_27MO = 2
#    RH028_28MO = 3
#
#    # RHEL for SAP HANA|High-Availability Add-On|Extended Update Support (EUS)|\
#    # Update Services for SAP Solutions (E4S)" (diagnostic)
#    #  RH028_32MO: int = 3  # 0=< x <9
#    #  RH028_33MO: int = 4  # 9=< x <128
#    #  RH028_34MO: int = 5  # 128>
#
#    RH028_32MO = 4
#    RH028_33MO = 5
#    RH028_34MO = 6


# NOTE: Class which solemny hold data, nothing else
@dataclass(slots=True, eq=False, match_args=False, init=False)
class RHsystemprofile:
    ansible: dict[str, Any] | None
    arch: str | None
    basearch: str | None
    bios_release_date: str | None
    bios_vendor: str | None
    bios_version: str | None
    bootc_status: dict[str, Any] | None
    captured_date: str | None
    cloud_provider: str | None
    conversions: dict[str, Any] | None
    cores_per_socket: str | None
    cpu_flags: list[str] | None
    cpu_model: str | None
    disk_devices: list[Any] | None
    dnf_modules: list[Any] | None
    enabled_services: list[Any] | None
    gpg_pubkeys: list[Any] | None
    greenboot_fallback_detected: bool | None
    greenboot_status: str | None
    host_type: str | None
    image_builder: dict[str, Any] | None
    infrastructure_type: str | None
    infrastructure_vendor: str | None
    insights_client_version: str | None
    insights_egg_version: str | None
    installed_packages: list[Any] | None
    installed_packages_delta: list[Any] | None
    installed_products: list[Any] | None
    installed_services: list[Any] | None
    intersystems: dict[str, Any] | None
    is_marketplace: bool | None
    katello_agent_running: bool | None
    kernel_modules: list[Any] | None
    last_boot_time: str | None
    mssql: dict[str, Any] | None
    network_interfaces: list[Any] | None
    number_of_cpus: int | None
    number_of_sockets: int | None
    operating_system: dict[str, Any] | None
    os_kernel_version: str | None
    os_release: str | None
    owner_id: str | None
    public_dns: list[Any] | None
    public_ipv4_addresses: list[Any] | None
    releasever: str | None
    rhc_client_id: str | None
    rhc_config_state: str | None
    rhel_ai: dict[str, Any] | None
    rhsm: dict[str, Any] | None
    rpm_ostree_deployments: list[Any] | None
    running_processes: list[Any] | None
    sap: dict[str, Any] | None
    sap_instance_number: str | None
    sap_sids: list[Any] | None
    sap_system: bool | None
    sap_version: str | None
    satellite_managed: bool | None
    selinux_config_file: str | None
    selinux_current_mode: str | None
    subscription_auto_attach: str | None
    subscription_status: str | None
    system_memory_bytes: int | None
    system_purpose: dict[str, Any] | None
    system_update_method: str | None
    systemd: dict[str, Any] | None
    third_party_services: str | None
    threads_per_core: int | None
    tuned_profile: str | None
    virtual_host_uuid: str | None
    yum_repos: list[Any] | None

    def __init__(self, **kwargs) -> None:
        for slot in self.__slots__:
            if (value := kwargs.get(slot)) is not None:
                setattr(self, slot, value)
            else:
                setattr(self, slot, None)


@dataclass(slots=True, eq=False)
class RHhost:
    id: str
    insights_id: str
    fqdn: str
    display_name: str
    org_id: str = ""
    mac_addresses: list[str] = field(default_factory=list)
    ip_addresses: list[str] = field(default_factory=list)
    systemprofile: RHsystemprofile | None = None

    def __eq__(self, other: object):
        if isinstance(other, RHhost):
            return self.id == other.id
        raise TypeError
