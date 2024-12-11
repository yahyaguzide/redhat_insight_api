"""
Custom RedHat Response Object
"""

from dataclasses import dataclass, field, InitVar
from json import loads, JSONDecodeError
from typing import Any

from .rh_exceptions import RHJSONDecodeError


@dataclass
class RHresponse:
    status_code: int
    headers: dict[str, str]
    reason: str
    url: str
    content: InitVar[str] = field(default="")
    _content: str = field(init=False)

    def __post_init__(self, content) -> None:
        self._content = content

    @property
    def ok(self) -> bool:
        """
        Returns True if status_code is less than 400

        returns: bool
        """

        return True if self.status_code < 400 else False

    @property
    def text(self) -> str:
        """
        Returns response content.

        returns: str
        """

        return self._content

    @property
    def json(self) -> dict[str, Any]:
        """
        Returns content as json

        returns: dict
        """

        try:
            return loads(self._content)
        except JSONDecodeError:
            raise RHJSONDecodeError
