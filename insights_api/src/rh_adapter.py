"""Adapter for RedHat Insights"""

from dataclasses import InitVar, dataclass, field

from enum import Enum

from requests import Session, Response
from .rh_exceptions import (
    RHAPIConnectionError,
    RHAPINoTokenError,
)
from insights_api.utils._internal_utils import join_url_str, cleanup_url_str


class Actions(Enum):
    get = 1
    delete = 2
    put = 3
    patch = 4
    post = 5


@dataclass(repr=False, eq=False)
class RHadapter:
    """
    Adapter for the RedHat Insight API.
    Methods like get post delete are predefined here.

    API key eventually run out of time, to get a new API Token use refresh_api_token()
    """

    refresh_token: InitVar[str | None] = field(default=None)
    api_token: InitVar[str | None] = field(default=None)
    _refresh_token: str | None = field(init=False)
    _api_token: str | None = field(init=False)
    base_url: str = field(default="https://console.redhat.com/api")
    session: Session = field(default_factory=Session)
    refresh_url: str = field(
        default="https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"
    )
    headers: dict[str, str] = field(default_factory=dict)

    def __post_init__(self, refresh_token, api_token) -> None:
        """Post init"""

        self._refresh_token = refresh_token
        self._api_token = api_token

        self.base_url = cleanup_url_str(self.base_url)
        self.refresh_url = cleanup_url_str(self.refresh_url)

        # NOTE: Allow API token to be set individually
        if not self._api_token:
            self.refresh_api_token()
        else:
            # NOTE: Set header if only api_token is given
            self.headers = {"Authorization": f"Bearer {self._api_token}"}

    def close(self) -> None:
        self.session.close()

    def refresh_api_token(self) -> None:
        """Refresh the access token and save it to the api_token variable"""

        if self._refresh_token is None:
            raise RHAPINoTokenError("No Refresh Token set")

        data = {
            "refresh_token": self._refresh_token,
            "client_id": "rhsm-api",
            "grant_type": "refresh_token",
        }
        if (
            response := self.session.post(url=str(self.refresh_url), data=data)
        ).status_code == 200:
            self._api_token = response.json()["access_token"]
            self.headers = {"Authorization": f"Bearer {self._api_token}"}
            return
        raise RHAPIConnectionError(
            "Can't get new Access token from " + str(self.refresh_url)
        )

    def _do_put_patch_post_get(
        self,
        action: Actions,
        endpoint: str,
        params: dict[str, str] | None = None,
        #        data: dict[str, Any] | None = None,
        json: dict[str, str] | None = None,
    ) -> Response:
        """
        Make requests to the API

        param action (str): Wich request to make

        returns: requests.Response
        """

        if self._api_token is None:
            raise RHAPINoTokenError("No API Token set")

        url = join_url_str(self.base_url, endpoint)
        return self.session.request(
            method=action.name,
            url=url,
            headers=self.headers,
            params=params,
            #            data=data,
            json=json,
        )

    def get(self, endpoint: str, params: dict[str, str] | None = None) -> Response:
        """
        get request to the API endpoint

        param endpoint (str): Endpoint to concat with the base url address
        param params (dict): Query parameters to the Endpoint

        returns: request.Response
        """

        return self._do_put_patch_post_get(
            action=Actions.get, endpoint=endpoint, params=params, json=None
        )

    def delete(self, endpoint: str, params: dict[str, str] | None = None) -> Response:
        """
        delete request to the API endpoint

        param endpoint (str): Endpoint to concat with the base url address
        param params (dict): Query parameters to the Endpoint

        returns: request.Response
        """

        return self._do_put_patch_post_get(
            action=Actions.delete, endpoint=endpoint, params=params, json=None
        )

    def put(
        self,
        endpoint: str,
        params: dict[str, str] | None = None,
        json: dict[str, str] | None = None,
    ) -> Response:
        """
        put request to the API endpoint

        param endpoint (str): Endpoint to concat with the base url address
        param params (dict): Query parameters to the Endpoint
        param json (dict): Json payload for the request

        returns: request.Response
        """

        return self._do_put_patch_post_get(
            action=Actions.put, endpoint=endpoint, params=params, json=json
        )

    def patch(
        self,
        endpoint: str,
        params: dict[str, str] | None = None,
        json: dict[str, str] | None = None,
    ) -> Response:
        """
        patch request to the API endpoint

        param endpoint (str): Endpoint to concat with the base url address
        param params (dict): Query parameters to the Endpoint
        param json (dict): Json payload for the request

        returns: request.Response
        """

        return self._do_put_patch_post_get(
            action=Actions.patch, endpoint=endpoint, params=params, json=json
        )

    def post(
        self,
        endpoint: str,
        params: dict[str, str] | None = None,
        json: dict[str, str] | None = None,
    ) -> Response:
        """
        post request to the API endpoint

        param endpoint (str): Endpoint to concat with the base url address
        param params (dict): Query parameters to the Endpoint
        param json (dict): Json payload for the request

        returns: request.Response
        """

        return self._do_put_patch_post_get(
            action=Actions.patch, endpoint=endpoint, params=params, json=json
        )
