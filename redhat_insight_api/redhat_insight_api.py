"""
RedHat API wrapper to request data from RedHat

Author: Yahya Güzide
Date: 2024.11.29
"""

from dataclasses import KW_ONLY, dataclass, field

from redhat_insight_api.src import redhat_insights_adapter
from redhat_insight_api.src.redhat_insights_adapter import RedHatInsightAdapter
from redhat_insight_api.src.redhat_insights_inventory import RedHatInventories


@dataclass(repr=False, unsafe_hash=False, eq=False, match_args=False, kw_only=True)
class RedHatInsightAPI:
    adapter: RedHatInsightAdapter

    inventories: RedHatInventories = field(init=False)
    # TODO: Rest of the API endpoints
    # ...
