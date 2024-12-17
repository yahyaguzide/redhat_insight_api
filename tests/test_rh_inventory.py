import pytest
from unittest.mock import Mock, patch

from insights_api.src import rh_adapter
from insights_api.src.rh_adapter import RHadapter
from insights_api.src.rh_inventory import RHinventory


api_token = "test"
refresh_token = "test"


@pytest.fixture(scope="class")
def rhadapter() -> RHadapter:
    global api_token
    global refresh_token
    return RHadapter(refresh_token=refresh_token, api_token=api_token)


@pytest.fixture(scope="function")
def mock_response():
    global api_token
    global refresh_token

    mock_response = Mock()
    mock_response.json.return_value = {"test": "mock_response"}
    mock_response.status_code = 200
    mock_response.content = '{"test": "mock_response"}'
    mock_response.url = "test/url"
    mock_response.reason = "test reason"
    mock_response.headers = {"Authorization": f"Bearer {api_token}"}

    return mock_response


class TestHosts:
    global api_token
    global refresh_token

    @patch.object(rh_adapter.Session, "request")
    def test_get_hosts(self, mock_request, mock_response, rhadapter) -> None:
        mock_request.return_value = mock_response
        rhinventory = RHinventory(rhadapter)

        response = rhinventory.get_hosts()

        mock_request.assert_called_with(
            method="get",
            url="https://console.redhat.com/api/inventory/v1/hosts",
            headers={"Authorization": f"Bearer {api_token}"},
            params={},
            json=None,
        )

        assert response.text == mock_response.content
        assert response.json == mock_response.json()
        assert response.status_code == mock_response.status_code
        assert response.url == mock_response.url
        assert response.headers == mock_response.headers

    @patch.object(rh_adapter.Session, "request")
    def test_get_hosts_system_profile(
        self, mock_request, mock_response, rhadapter
    ) -> None:
        mock_request.return_value = mock_response
        rhinventory = RHinventory(rhadapter)

        for response in rhinventory.get_hosts_system_profile("test1", "test2"):
            mock_request.assert_called_with(
                method="get",
                url="https://console.redhat.com/api/inventory/v1/hosts/test1,test2/system_profile",
                headers={"Authorization": f"Bearer {api_token}"},
                params={},
                json=None,
            )

            assert response.text == mock_response.content
            assert response.json == mock_response.json()
            assert response.status_code == mock_response.status_code
            assert response.url == mock_response.url
            assert response.headers == mock_response.headers
