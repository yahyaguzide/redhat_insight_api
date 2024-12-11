"""
Base Clase for all Endpoint Classes
"""

from dataclasses import dataclass

from .rh_adapter import RHadapter


@dataclass(repr=False, eq=False, kw_only=True)
class RHendpointBase:
    """Base class for RedHat Endpoints"""

    endpoint: str
    adapter: RHadapter
