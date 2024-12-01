"""
RedHat API wrapper to request data from RedHat

Author: Yahya Güzide
Date: 2024.11.29
"""

from dataclasses import dataclass, field
# import json
from functools import partial
from itertools import islice

import requests

# from retrying import retry


# Exception for RedHat API access
class RHAPIConnectionError(Exception):
    """Connection Error for RedHat API"""

    pass


@dataclass(repr=False, eq=False, order=False, unsafe_hash=False, frozen=False)
class RedHatAPI:
    """
    Class that wrapps around the API of RedHat Insights. Close the Session with close_session().

        Parameters:
            _session (requests.session): Session Object
            _refresh_token (str): The refresh token to create a API Token
            _api_token (str): The API Token
            _base_url (str): Base url for API queries
            _refresh_url (str): The url to refresh the API Token
            _headers (dict[str: any]): header for the API requests
    """

    _session: requests.Session
    _refresh_token: str
    _api_token: str
    _base_url: str
    _refresh_url: str
    _headers: dict[str:str] = field(default_factory=dict)

    def __post_init__(self):
        self._session = requests.session()

        # Get api token
        self.refresh_api_token()
        self._headers: dict[str, str] = {"Authorization": f"Bearer {self._api_token}"}

    def refresh_api_token(self) -> None:
        """
        Refresh the access token and save it to the api_token variable
        """

        data = {
            "refresh_token": self._refresh_token,
            "client_id": "rhsm-api",
            "grant_type": "refresh_token",
        }
        if (response := self._session.post(url=self._refresh_url, data=data)).status_code == 200:
            self._api_token = response.json()["access_token"]
            return
        raise RHAPIConnectionError("Can't get new Access token from " + self._refresh_url)

    @staticmethod
    def __chunk_list(lst, chunk_size) -> list:
        iterator = iter(lst)
        return list(iter(lambda: list(islice(iterator, chunk_size)), []))

    ###############################
    # Inventory Application
    ###############################

    def inventory_get_hosts(self, per_page: int = 100, page: int = 1) -> list[dict[str:any]]:
        """
        Return Host data from the redhat inventory
        """

        url: str = f"{self._base_url}inventory/v1/hosts?per_page={per_page}&page={page}"
        headers: dict[str, str] = {"Authorization": f"Bearer {self._api_token}"}

        if (response := self._session.get(url=url, headers=headers)).status_code == 200:
            return response.json()["results"]
        raise RHAPIConnectionError("Connection not possible, cant get hosts from " + url)

    def inventory_get_all_hosts(self) -> list[dict[str:any]]:
        """
        Return all Hosts from Insights Inventory

            Retruns: list[dict[str: any]]
        """

        page: int = 0
        hosts: list[dict[str:any]] = []

        next_page: bool = True
        while next_page:
            page += 1
            try:
                hosts.extend(self.inventory_get_hosts(page=page))
            except ConnectionError:
                next_page = False
        return hosts

    def get_hosts_details(
        self, host_id: str, *host_ids: str, append_str: str = None
    ) -> list[dict[str:any]]:
        """
        Default is to get host_profile details if append_str is not empty try to get data
        :param host_id: first host_profile id, at least one must be given
        :param host_ids: Additional ids
        :param append_str: additional api address
        :return: returns list of dicts
        """
        id_list: list[str] = [host_id] + list(host_ids)
        tmp_list: list[dict[str:any]] = []

        # I think Redhat can't handle nearly 400 Host_ids
        for id_list_chunk in self.__chunk_list(id_list, 100):
            hosts_str: str = ",".join(id_list_chunk)
            url = f"{self._base_url}inventory/v1/hosts/{hosts_str}"
            if append_str is not None:
                url += f"/{append_str}"

            if (response := self._session.get(url=url, headers=self._headers)).status_code == 200:
                tmp_list.extend(response.json()["results"])
            else:
                raise ConnectionError("Not able to read host_profile details from " + url)
        return tmp_list

    #    @lru_cache(maxsize=100)
    @staticmethod
    def __make_host_system_data_obj(
        hid: str,
        number_of_cpus: int,
        cores_per_socket: int,
        system_memory_bytes: int,
        repos: frozenset,
    ) -> dict[str:any]:
        tmp_host: dict[str:any] = {
            "id": hid,
            "number_of_cpus": number_of_cpus,
            "cores_per_socket": cores_per_socket,
            "system_memory_bytes": system_memory_bytes,
            "enabled_repos": [],
        }
        for repo in repos:
            if repo[1]:
                tmp_host["enabled_repos"].append(repo[0])
        return tmp_host

    def get_system_data(self, host: dict[str:any], *hosts: dict[str:any]) -> list[dict]:
        host_list = [host] + list(hosts)

        tmp_host_list: list[dict[str:any]] = []
        for host in host_list:
            tmp_host = self.__make_host_system_data_obj(
                host["id"],
                host["system_profile"].get("number_of_cpus"),
                host["system_profile"].get("cores_per_socket"),
                host["system_profile"].get("system_memory_bytes"),
                frozenset(
                    [
                        (repo["id"], repo.get("enabled"))
                        for repo in host["system_profile"]["yum_repos"]
                    ]
                    if host["system_profile"].get("yum_repos")
                    else []
                ),
            )

            tmp_host_list.append(tmp_host)
        return tmp_host_list

    def close_session(self):
        self._session.close()
