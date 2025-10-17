from typing import Iterable


def concat_strings(items: Iterable[str]) -> str:
    """
    Concatenate an iterable of items into a single string efficiently.

    Performance and robustness fix:
    - Convert each item to string to avoid TypeError on non-string values.
    - Use str.join on a generator to achieve O(n) concatenation.
    """
    return "".join(str(item) for item in items)
