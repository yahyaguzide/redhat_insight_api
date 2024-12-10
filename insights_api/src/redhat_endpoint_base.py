"""
Base Clase for all Endpoint Classes
"""

from dataclasses import dataclass

from insights_api.src.redhat_insights_adapter import RedHatInsightAdapter
from insights_api.utils.helper_types import URLstr


@dataclass(repr=False, eq=False, kw_only=True)
class RedHatEndpointBase:
    """Base class for RedHat Endpoints"""

    endpoint: URLstr
    adapter: RedHatInsightAdapter
