from collections.abc import Generator
from itertools import islice


@staticmethod
def list_to_chunks(lst: list[str], chunk_size: int) -> Generator:
    iterator = iter(lst)
    while (chunk := list(islice(iterator, chunk_size))) is not None:
        yield chunk


#   return list(iter(lambda: list(islice(iterator, chunk_size)), []))
