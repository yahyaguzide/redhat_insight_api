import pytest
from unittest.mock import Mock, patch

import requests

from insights_api.src import redhat_insights_adapter
from insights_api.src.redhat_insights_adapter import RedHatInsightAdapter
from insights_api.src.redhat_insights_exceptions import (
    RHAPIConnectionError,
    RHAPINoTokenError,
)


@pytest.fixture
def refresh_token():
    return "mock_refresh_token"


@pytest.fixture
def api_token():
    return "mock_api_token"


@pytest.fixture
def full_url():
    return "https://console.redhat.com/api/test"


class Test_adapter_init_refresh:
    @pytest.fixture
    def mock_response(self):
        mock_response = Mock()
        mock_response.json.return_value = {"access_token": "mock_api_token"}
        mock_response.status_code = 200

        return mock_response

    @patch.object(requests.Session, "post")
    def test_init_api_refresh_token(
        self, mock_post, mock_response, refresh_token, api_token
    ):
        mock_post.return_value = mock_response

        RedHatInsightAdapter(refresh_token=refresh_token, api_token=api_token)

        # TEST: Make sure post was not called
        mock_response.assert_not_called()

    @patch.object(redhat_insights_adapter.Session, "post")
    def test_init_refresh_token(
        self, mock_post, mock_response, refresh_token, api_token
    ):
        mock_post.return_value = mock_response

        tmp_adapter = RedHatInsightAdapter(refresh_token=refresh_token)

        # TEST: Was post called once
        mock_post.assert_called_once()

        # TEST: api_token variable is set correctly
        assert tmp_adapter._api_token == api_token, "API Token not correcty set"

        # TEST: Header is set correctly
        assert tmp_adapter.headers == {
            "Authorization": f"Bearer {api_token}"
        }, "Headers not correctly set"

    @patch.object(redhat_insights_adapter.Session, "post")
    def test_init_refresh_token_is_none(self, mock_post, mock_response):
        mock_post.return_value = mock_response

        try:
            RedHatInsightAdapter()
        except RHAPINoTokenError:
            return
        except Exception as e:
            assert False, f"Wrong exception raised {e}"
        assert False, "No Exception raised"


class Test_do_pu_patch_post_get:
    @pytest.fixture
    def mock_response(self):
        mock_response = Mock()
        mock_response.json.return_value = {"test": "mock_response"}
        mock_response.status_code = 200

        return mock_response

    @patch.object(redhat_insights_adapter.Session, "request")
    def test_api_token_is_none(self, mock_request, mock_response, api_token):
        mock_request.return_value = mock_response

        tmp_adapter = RedHatInsightAdapter(api_token=api_token)
        tmp_adapter._api_token = None

        try:
            tmp_adapter._do_put_patch_post_get(
                action=redhat_insights_adapter.Actions.get, endpoint="test"
            )
        except RHAPINoTokenError:
            return
        except Exception as e:
            assert False, f"Wrong exception raise {e}"
        assert False, "No Exception raised"

    @patch.object(redhat_insights_adapter.Session, "request")
    def test_get(self, mock_request, mock_response, api_token, full_url):
        mock_request.return_value = mock_response

        tmp_adapter = RedHatInsightAdapter(api_token=api_token)

        response = tmp_adapter._do_put_patch_post_get(
            action=redhat_insights_adapter.Actions.get, endpoint="test"
        )

        mock_request.assert_called_with(
            method="get",
            url=full_url,
            headers={"Authorization": f"Bearer {api_token}"},
            params=None,
            json=None,
        )
        assert response.status_code == 200
        assert response.json()["test"] == "mock_response"

    @patch.object(redhat_insights_adapter.Session, "request")
    def test_put(self, mock_request, mock_response, api_token, full_url):
        mock_request.return_value = mock_response

        tmp_adapter = RedHatInsightAdapter(api_token=api_token)

        params = {"test": "test"}
        json = {"test": "test"}

        response = tmp_adapter._do_put_patch_post_get(
            action=redhat_insights_adapter.Actions.put,
            endpoint="test",
            params=params,
            json=json,
        )

        mock_request.assert_called_with(
            method="put",
            url=full_url,
            headers={"Authorization": f"Bearer {api_token}"},
            params=params,
            json=json,
        )
        assert response.status_code == 200
        assert response.json()["test"] == "mock_response"

    @patch.object(redhat_insights_adapter.Session, "request")
    def test_patch(self, mock_request, mock_response, api_token, full_url):
        mock_request.return_value = mock_response

        tmp_adapter = RedHatInsightAdapter(api_token=api_token)

        params = {"test": "test"}
        json = {"test": "test"}

        response = tmp_adapter._do_put_patch_post_get(
            action=redhat_insights_adapter.Actions.patch,
            endpoint="test",
            params=params,
            json=json,
        )

        mock_request.assert_called_with(
            method="patch",
            url=full_url,
            headers={"Authorization": f"Bearer {api_token}"},
            params=params,
            json=json,
        )
        assert response.status_code == 200
        assert response.json()["test"] == "mock_response"

    @patch.object(redhat_insights_adapter.Session, "request")
    def test_post(self, mock_request, mock_response, api_token, full_url):
        mock_request.return_value = mock_response

        tmp_adapter = RedHatInsightAdapter(api_token=api_token)

        params = {"test": "test"}
        json = {"test": "test"}

        response = tmp_adapter._do_put_patch_post_get(
            action=redhat_insights_adapter.Actions.post,
            endpoint="test",
            params=params,
            json=json,
        )

        mock_request.assert_called_with(
            method="post",
            url=full_url,
            headers={"Authorization": f"Bearer {api_token}"},
            params=params,
            json=json,
        )
        assert response.status_code == 200
        assert response.json()["test"] == "mock_response"


class Test_put_patch_post_get:
    @patch.object(redhat_insights_adapter.Session, "request")
    def test_put(self, refresh_token, api_token):
        pass
