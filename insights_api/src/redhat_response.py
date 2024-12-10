"""
Custom RedHat Response Object
"""

from dataclasses import dataclass, field, InitVar
from json import dumps


@dataclass
class RHresponse:
    status_code: int
    headers: dict[str, str]
    reason: str
    url: str
    json: InitVar[dict[str, str]]
    _json: dict[str, str] = field(init=False, default_factory=dict)
    _text: str | None = field(init=False, default=None)

    def __post_init__(self, json) -> None:
        self._json = json

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
        Returns string of json and sets _json if not already set.

        returns: str
        """

        if self._text is None:
            self._text = dumps(self._json)
        return self._text
