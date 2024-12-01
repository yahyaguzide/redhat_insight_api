"""Collection of Classes to ease Development"""

from __future__ import annotations


class URLstr:
    """Helper to manage URLS"""

    _url: str

    def __init__(self, url) -> None:
        self.url = url

    @property
    def url(self) -> str:
        """getter for url"""

        return self._url

    @url.setter
    def url(self, u: str) -> None:
        """setter for url"""

        self._url = buf if (buf := u.strip())[-1] != "/" else buf[:-1]

    def join(self, u: str | URLstr) -> URLstr:
        """
        join url with the local one

        param u (str): url to join
        return: New URLstr with updated url
        """

        return URLstr(self._url + f"/{u}")

    def __add__(self, other: str | URLstr) -> URLstr:
        """
        join url with the local one

        param other (str): url to join
        return: New URLstr with updated url
        """

        return self.join(other)

    def __str__(self) -> str:
        """Parse to string"""

        return self._url

    def __repr__(self) -> str:
        """Returns the url"""

        return self._url

    def __eq__(self, value: object) -> bool:
        """Check if the URL is the Same"""

        if isinstance(value, URLstr):
            return self._url == value.url
        return NotImplemented
