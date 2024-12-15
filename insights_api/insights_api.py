"""
RedHat API wrapper to request data from RedHat

Author: Yahya Güzide
Date: 2024.11.29
"""

from dataclasses import dataclass, field

from insights_api.src.rh_adapter import RHadapter
from insights_api.src.rh_inventory import RHInventories


@dataclass(repr=False, unsafe_hash=False, eq=False, match_args=False, kw_only=True)
class RedHatInsightAPI:
    adapter: RHadapter

    _inventories: RHInventories | None = field(init=False, default=None)
    # TODO: Rest of the API endpoints
    # ...

    @property
    def inventories(self) -> RHInventories:
        if self._inventories is None:
            self._inventories = RHInventories(adapter=self.adapter)
        return self._inventories
