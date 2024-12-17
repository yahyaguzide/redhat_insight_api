"""
Tools to gather and work with hosts
"""

from insights_api.src.rh_host import RHhost

from insights_api.src.rh_inventory import RHinventory


def get_all_hosts(inventories: RHinventory) -> list[RHhost]:
    host_objs = []

    page = 0
    while (
        response := inventories.get_hosts(
            per_page=100,
            page=page,
            fields="id,insights_id,fqdn,display_name,org_id,mac_addresses,ip_addresses",
        )
    ).status_code == 200:
        tmp = response.json["results"]
        for h in tmp:
            host_objs.append(RHhost(**h))
    #                RHhost(
    #                    id=h["id"],
    #                    insights_id=h["insights_id"],
    #                    fqdn=h["fqdn"],
    #                    display_name=h["display_name"],
    #                    org_id=h["org_id"],
    #                    mac_addresses=h["mac_addresses"],
    #                    ip_addresses=h["ip_addresses"],
    #                )
    #            )
    return host_objs


def populate_systemprofiles(inventories: RHinventory, hosts: list[RHhost]) -> None:
    """
    Read all Systemprofiles and write them to the host objects
    """

    tmp_hosts = {str(h.id): h for h in hosts}

    for response in inventories.get_hosts_system_profile(*tmp_hosts.keys()):
        for profile in response.json["results"]:
            tmp_hosts[profile["id"]].set_systemprofile(profile)
