from collections.abc import Generator
from itertools import islice


@staticmethod
def list_to_chunks(lst: list[str], chunk_size: int) -> Generator[list[str]]:
    it = iter(lst)
    while not (chunk := list(islice(it, chunk_size))):
        yield chunk


def cleanup_url_str(url: str) -> str:
    """
    clean up a string that represents a url

    param url (str): string which hold the url

    returns: str
    """
    return url.strip().strip("/")


def join_url_str(url_a: str, url_b: str) -> str:
    """
    join two url strings

    param url_a (str): first url
    param url_b (str): second url

    returns: str
    """

    return url_a + f"/{url_b}"
