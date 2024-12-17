"""
RedHat Insights Inventory endpoint
Documentation: https://console.redhat.com/docs/api/inventory/v1#operations-accounts_staleness-api%5C.staleness%5C.delete_staleness
"""

from collections.abc import Generator
from .rh_endpointbase import RHendpointBase
from .rh_adapter import RHadapter
from .rh_response import RHresponse
from insights_api.utils._internal_utils import (
    list_to_chunks,
    join_url_str,
)


class RHinventory(RHendpointBase):
    """Inventories Endpoint for RedHat Insights API"""

    def __init__(self, adapter: RHadapter) -> None:
        super().__init__(adapter=adapter, endpoint="inventory/v1")

    # """""""""""""""""""""""""""""""""""
    # account_staleness
    # """""""""""""""""""""""""""""""""""
    def delete_account_staleness(self):
        # TODO: finish me
        pass

    def get_account_staleness(self):
        # TODO: finish me
        pass

    def patch_account_staleness(self):
        # TODO: finish me
        pass

    def post_account_staleness(self):
        # TODO: finish me
        pass

    def get_account_staleness_default(self):
        # TODO: finish me
        pass

    # """""""""""""""""""""""""""""""""""
    # groups
    # """""""""""""""""""""""""""""""""""
    def get_groups(self):
        # TODO: finish me
        pass

    def post_groups(self):
        # TODO: finish me
        pass

    def delete_groups_by_host_id(self):
        # TODO: finish me
        pass

    def delete_groups_by_group_id(self):
        # TODO: finish me
        pass

    def get_groups_by_group_id(self):
        # TODO: finish me
        pass

    def patch_groups_by_group_id(self):
        # TODO: finish me
        pass

    def post_add_hosts_to_group(self):
        # TODO: finish me
        pass

    def delte_hosts_from_group(self):
        # TODO: finish me
        pass

    # """""""""""""""""""""""""""""""""""
    # hosts
    # """""""""""""""""""""""""""""""""""

    def get_host_exists(self, insights_id: str) -> RHresponse:
        """
        Find one host by insights_id, if it exists.

        Required permissions: inventory:hosts:read

        Status Codes:
            200: Matching Host found
            400: Invalud requests
            404: Host not found
            409: Multiple matching hosts detected

        param insights_id (str): The Inisghts ID of the host

        returns: RHresponse
        """

        path = "host_exists"
        response = self.adapter.get(
            endpoint=join_url_str(self.endpoint, path),
            params={"insights_id": insights_id},
        )
        return RHresponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            reason=response.reason,
            url=response.url,
            content=response.text,
        )

    def delete_hosts(self, **params) -> RHresponse:
        """
        Delete the entire list of hosts filtered by the given parameters.

        Required permissions: inventory:hosts:write

        Status Codes:
            202: Request for deletion of filtered hosts has been accepted
            400: Invalid request

        param **params: List of Parameters
            Accepted values:
                display_name
                fqdn
                hostname_or_id
                insights_id
                provider_id
                provider_type
                updated_start
                updated_end
                group_name
                registered_with
                staleness
                tags
                filter

        returns: RHresponse
        """
        path = "hosts"
        response = self.adapter.delete(
            endpoint=join_url_str(self.endpoint, path), params=params
        )
        return RHresponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            reason=response.reason,
            url=response.url,
            content=response.text,
        )

    def get_hosts(self, **params) -> RHresponse:
        """
        Read the list of hosts available to the account.
        To get all Hosts iterate over all pages.

        Required permissions: inventory:hosts:read

        Status Codes:
            200: Successfully read the hosts list

        param **params: List of Parameters
            Accepted values:
                display_name
                fqdn
                hostname_or_id
                insights_id
                provider_id
                provider_type
                updated_start
                updated_end
                group_name
                branch_id
                per_page
                page
                order_by
                order_how
                registered_with
                staleness
                tags
                filter
                fields

        returns: RHresponse
        """
        path = "hosts"
        response = self.adapter.get(
            endpoint=join_url_str(self.endpoint, path), params=params
        )
        return RHresponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            reason=response.reason,
            url=response.url,
            content=response.text,
        )

    def delete_all_hosts(self, confirm_delete_all: bool = False) -> RHresponse:
        """
        Delete all hosts on the account. The request must include "confirm_delete_all=true".
        Commented out for now!!!

        Required permissions: inventory:hosts:write

        Status Codes:
            202: Request for deleting all hosts been accepted
            400: Invalid request


        returns: RHresponse
        """
        path = "hosts/all"
        #        response = self.adapter.delete(
        #            endpoint=join_url_str(self.endpoint, path)),
        #            params={"confirm_delete_all": str(confirm_delete_all)},
        #        )
        #        return RHresponse(
        #            status_code=response.status_code,
        #            headers=dict(response.headers),
        #            reason=response.reason,
        #            url=response.url,
        #            content=response.text,
        #        )
        return RHresponse(
            status_code=404,
            headers={},
            reason="Not implemented yet",
            url="",
            content="",
        )

    def post_host_checkin(self, json: dict[str, str]) -> RHresponse:
        """
        Finds a host and updates its staleness timestamps. It uses the supplied canonical facts to determine which host to update. By default, the staleness timestamp is set to 1 hour from when the request is received; however, this can be overridden by supplying the interval.

        Required permissions: inventory:hosts:write

        Status Codes:
            404: Not found

        param json (dict): Json object to send in the Request body

        returns: RHresponse
        """

        path = "host/checkin"
        response = self.adapter.post(
            endpoint=join_url_str(self.endpoint, path), json=json
        )
        return RHresponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            reason=response.reason,
            url=response.url,
            content=response.text,
        )

    def delete_hosts_by_id(
        self, host: str, *hosts: str, branch_id: str
    ) -> Generator[RHresponse]:
        """
        Delete hosts by IDs. Accepts Hosts as Parameters.

        Required permissions: inventory:hosts:write

        Status Codes:
            200: Successfully deleted hosts
            400: Invalid request
            404: Host not found

        param host (str): host ID
        param *hosts (str): host IDs
        param branch_id (str): Filter by branch_id

        returns: Generator[RHresponse]
        """

        path = "hosts"
        for host_chunk in list_to_chunks([host] + list(hosts), 50):
            hosts_ids = ",".join(host_chunk)
            response = self.adapter.delete(
                endpoint=join_url_str(self.endpoint, f"{path}/{hosts_ids}"),
                params={"branch_id": branch_id},
            )
            yield RHresponse(
                status_code=response.status_code,
                headers=dict(response.headers),
                reason=response.reason,
                url=response.url,
                content=response.text,
            )

    def get_hosts_by_id(self, host: str, *hosts, **params) -> Generator[RHresponse]:
        """
        Find one or more hosts by their ID.

        Required permissions: inventory:hosts:read

        Status Codes:
            200: Successfully searched for hosts
            400: Invalid request
            404: Host not found

        param host (str): host ID
        param *hosts (str): host IDs
        param **params: List of parameters
            accepted values:
                branch_id
                per_page
                page
                order_by
                order_how
                fields

        returns: Generator[RHresponse]
        """

        path = "hosts"
        for host_chunk in list_to_chunks([host] + list(hosts), 50):
            hosts_ids = ",".join(host_chunk)
            response = self.adapter.get(
                endpoint=join_url_str(self.endpoint, f"{path}/{hosts_ids}"),
                params=params,
            )
            yield RHresponse(
                status_code=response.status_code,
                headers=dict(response.headers),
                reason=response.reason,
                url=response.url,
                content=response.text,
            )

    def patch_hosts_by_id(
        self, host: str, *hosts: str, branch_id: str, json: dict[str, str]
    ) -> Generator[RHresponse]:
        """
        Update hosts_ids

        Required permissions: inventory:hosts:write

        Status Code:
            200: Successfully updated the hosts
            400: Invalid request
            404: Host not found

        param host (str): host ID
        param *hosts (str): host IDs
        param branch_id (str): Filter by branch_id
        param json (dict): Json object to be send in the request body.
            A group of fields to be updated on the host

        returns: Generator[RHresponse]
        """

        path = "hosts"
        for host_chunk in list_to_chunks([host] + list(hosts), 50):
            hosts_ids = ",".join(host_chunk)
            response = self.adapter.patch(
                endpoint=join_url_str(self.endpoint, f"{path}/{hosts_ids}"),
                params={"branch_id": branch_id},
                json=json,
            )
            yield RHresponse(
                status_code=response.status_code,
                headers=dict(response.headers),
                reason=response.reason,
                url=response.url,
                content=response.text,
            )

    def patch_hosts_merge_facts_under_namespace(
        self,
        host: str,
        *hosts: str,
        namespace: str,
        json: dict[str, str],
        branch_id: str | None = None,
    ) -> Generator[RHresponse]:
        """
        Merge one or multiple hosts facts under a namespace.

        Required permissions: inventory:hosts:write

        Status Code:
            200: Successfully merged facts
            400: Invalid request
            404: Host or namespace not found

        param host (str): host ID
        param *hosts (str): host IDs
        param branch_id (str): Filter by branch_id
        param json (dict): Json object to be send in the request body.
            example:
                {
                  "fact1": "value1",
                  "fact2": "value2"
                }

        returns: Generator[RHresponse]
        """

        path = "hosts"
        for host_chunk in list_to_chunks([host] + list(hosts), 50):
            hosts_ids = ",".join(host_chunk)
            response = self.adapter.patch(
                endpoint=join_url_str(self.endpoint, f"{path}/{hosts_ids}/{namespace}"),
                params={"branch_id": branch_id} if branch_id else None,
                json=json,
            )
            yield RHresponse(
                status_code=response.status_code,
                headers=dict(response.headers),
                reason=response.reason,
                url=response.url,
                content=response.text,
            )

    def put_hosts_replace_facts_under_namespace(
        self,
        host: str,
        *hosts: str,
        namespace: str,
        json: dict[str, str],
        branch_id: str | None = None,
    ) -> Generator[RHresponse]:
        """
        Replace facts under a namespace

        Required permissions: inventory:hosts:write

        Status Code:
            200: Successfully replaced facts
            400: Invalid request
            404: Host or namespace not found

        param host (str): host ID
        param *hosts (str): host IDs
        param branch_id (str): Filter by branch_id
        param json (dict): Json object to be send in the request body.
            example:
                {
                  "fact1": "value1",
                  "fact2": "value2"
                }

        returns: Generator[RHresponse]
        """

        path = "hosts"
        for host_chunk in list_to_chunks([host] + list(hosts), 50):
            hosts_ids = ",".join(host_chunk)
            response = self.adapter.put(
                endpoint=join_url_str(self.endpoint, f"{path}/{hosts_ids}/{namespace}"),
                params={"branch_id": branch_id} if branch_id else None,
                json=json,
            )
            yield RHresponse(
                status_code=response.status_code,
                headers=dict(response.headers),
                reason=response.reason,
                url=response.url,
                content=response.text,
            )

    def get_hosts_system_profile(
        self, host: str, *hosts: str, **params
    ) -> Generator[RHresponse]:
        """
        Find one or more hosts by their ID and return the id and system profile

        Required permissions: inventory:hosts:read

        Status Code:
            200: Successfully searched for hosts
            400: Invalid request
            404: Host not found

        param host (str): host ID
        param *hosts (str): host IDs
        param **params: List of Parameters
            Accepted values:
                per_page
                page
                order_by
                order_how
                branch_id
                fields

        returns: Generator[RHresponse]
        """

        path = "hosts"
        for host_chunk in list_to_chunks([host] + list(hosts), 50):
            hosts_ids = ",".join(host_chunk)
            response = self.adapter.get(
                endpoint=join_url_str(
                    self.endpoint, f"{path}/{hosts_ids}/system_profile"
                ),
                params=params,
            )
            yield RHresponse(
                status_code=response.status_code,
                headers=dict(response.headers),
                reason=response.reason,
                url=response.url,
                content=response.text,
            )

    def get_hosts_tags(self, host: str, *hosts: str, **params) -> Generator[RHresponse]:
        """
        Get the tags on a host

        Required permissions: inventory:hosts:read

        Status Code:
            200: Successfully found tags
            400: Invalid request

        param host (str): host ID
        param *hosts (str): host IDs
        param **params: List of Parameters
            Accepted values:
                per_page
                page
                order_by
                order_how
                search

        returns: Generator[RHresponse]
        """

        path = "hosts"
        for host_chunk in list_to_chunks([host] + list(hosts), 50):
            hosts_ids = ",".join(host_chunk)
            response = self.adapter.get(
                endpoint=join_url_str(self.endpoint, f"{path}/{hosts_ids}/tags"),
                params=params,
            )
            yield RHresponse(
                status_code=response.status_code,
                headers=dict(response.headers),
                reason=response.reason,
                url=response.url,
                content=response.text,
            )

    def get_hosts_tags_count(
        self, host: str, *hosts: str, **params
    ) -> Generator[RHresponse]:
        """
        Get the number of tags on a host or hosts

        Required permissions: inventory:hosts:read

        Status Code:
            200: Successfully found tag count
            400: Invalid request

        param host (str): host ID
        param *hosts (str): host IDs
        param **params: List of Parameters
            Accepted values:
                per_page
                page
                order_by
                order_how

        returns: Generator[RHresponse]
        """

        path = "hosts"
        for host_chunk in list_to_chunks([host] + list(hosts), 50):
            hosts_ids = ",".join(host_chunk)
            response = self.adapter.get(
                endpoint=join_url_str(self.endpoint, f"{path}/{hosts_ids}/tags/count"),
                params=params,
            )
            yield RHresponse(
                status_code=response.status_code,
                headers=dict(response.headers),
                reason=response.reason,
                url=response.url,
                content=response.text,
            )

    # """""""""""""""""""""""""""""""""""
    # resource-types
    # """""""""""""""""""""""""""""""""""

    # """""""""""""""""""""""""""""""""""
    # system_profile
    # """""""""""""""""""""""""""""""""""

    # """""""""""""""""""""""""""""""""""
    # tags
    # """""""""""""""""""""""""""""""""""
