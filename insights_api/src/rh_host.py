"""
Custom Host Object for Redhat Hosts data.
"""

from dataclasses import dataclass, field
from enum import Enum
from json import loads


class rh_vm_categories(Enum):
    # Normal rhel category
    #  RH028_26MO: int = 0  # 0=< x <9
    #  RH028_27MO: int = 1  # 9=< x <128
    #  RH028_28MO: int = 2  # 128>

    RH028_26MO = 1
    RH028_27MO = 2
    RH028_28MO = 3

    # RHEL for SAP HANA|High-Availability Add-On|Extended Update Support (EUS)|\
    # Update Services for SAP Solutions (E4S)" (diagnostic)
    #  RH028_32MO: int = 3  # 0=< x <9
    #  RH028_33MO: int = 4  # 9=< x <128
    #  RH028_34MO: int = 5  # 128>

    RH028_32MO = 4
    RH028_33MO = 5
    RH028_34MO = 6


# NOTE: Class which solemny hold data, nothing else
class RHsystemprofile:
    ansible: str | None = None
    arch: str | None = None
    basearch: str | None = None
    bios_release_date: str | None = None
    bios_vendor: str | None = None
    bios_version: str | None = None
    bootc_status: str | None = None
    captured_date: str | None = None
    cloud_provider: str | None = None
    conversions: str | None = None
    cores_per_socket: str | None = None
    cpu_flags: str | None = None
    cpu_model: str | None = None
    disk_devices: str | None = None
    dnf_modules: str | None = None
    enabled_services: str | None = None
    gpg_pubkeys: str | None = None
    greenboot_fallback_detected: str | None = None
    greenboot_status: str | None = None
    host_type: str | None = None
    image_builder: str | None = None
    infrastructure_type: str | None = None
    infrastructure_vendor: str | None = None
    insights_client_version: str | None = None
    insights_egg_version: str | None = None
    installed_packages: str | None = None
    installed_packages_delta: str | None = None
    installed_products: str | None = None
    installed_services: str | None = None
    intersystems: str | None = None
    is_marketplace: str | None = None
    katello_agent_running: str | None = None
    kernel_modules: str | None = None
    last_boot_time: str | None = None
    mssql: str | None = None
    network_interfaces: str | None = None
    number_of_cpus: int | None = None
    number_of_sockets: int | None = None
    operating_system: str | None = None
    os_kernel_version: str | None = None
    os_release: str | None = None
    owner_id: str | None = None
    public_dns: str | None = None
    public_ipv4_addresses: str | None = None
    releasever: str | None = None
    rhc_client_id: str | None = None
    rhc_config_state: str | None = None
    rhel_ai: str | None = None
    rhsm: str | None = None
    rpm_ostree_deployments: str | None = None
    running_processes: str | None = None
    sap: str | None = None
    sap_instance_number: str | None = None
    sap_sids: str | None = None
    sap_system: str | None = None
    sap_version: str | None = None
    satellite_managed: str | None = None
    selinux_config_file: str | None = None
    selinux_current_mode: str | None = None
    subscription_auto_attach: str | None = None
    subscription_status: str | None = None
    system_memory_bytes: str | None = None
    system_purpose: str | None = None
    system_update_method: str | None = None
    systemd: str | None = None
    third_party_services: str | None = None
    threads_per_core: str | None = None
    tuned_profile: str | None = None
    virtual_host_uuid: str | None = None
    yum_repos: str | None = None

    # NOTE: If the ride is more fly, then you must buy.
    __slots__ = tuple(__annotations__)

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if __annotations__.get(key) is not None:
                setattr(self, key, value)


@dataclass(match_args=False)
class RHhost:
    id: str
    insights_id: str
    fqdn: str
    display_name: str
    org_id: str
    mac_addresses: list[str]
    ip_addressses: list[str]
    _category: rh_vm_categories | None = field(init=False, default=None)
    systemprofile: RHsystemprofile = field(
        init=False, repr=False, default_factory=RHsystemprofile
    )

    def __check_if_special(self) -> bool | None:
        if self.systemprofile.yum_repos is None:
            return None

        special_keywords: list[str] = ["sap-solutions", "highavailability", "eus"]
        for repo in loads(self.systemprofile.yum_repos):
            if repo.get("enabled") and any(kw in repo["id"] for kw in special_keywords):
                return True
        return False

    @property
    def category(self) -> rh_vm_categories | None:
        if self._category is None and self.systemprofile.number_of_cpus is not None:
            num_cores = self.systemprofile.number_of_cpus
            tmp_special = self.__check_if_special()
            if tmp_special is not None:
                tmp_cat = 0
                if 9 <= num_cores < 128:
                    tmp_cat = 1
                elif 128 <= num_cores:
                    tmp_cat = 2
                self._category = (
                    rh_vm_categories(tmp_cat + 3)
                    if tmp_special
                    else rh_vm_categories(tmp_cat)
                )
        return self._category

    def __eq__(self, other: object):
        if isinstance(other, RHhost):
            return self.id == other.id
        raise TypeError
