import math
from typing import Tuple


def pagination(page: int, offset: int, length: int) -> Tuple[int, int]:
    """
    Calculate the interval [start, end) for a page

    Parameters:
        page: Page to calculate the interval
        offset: Maximum amount of data inside the interval
        length: Total amount of data

    Return:
        tuple(int, int): Tuple with the start and end index of the pagination
    """

    total_pages = math.ceil(length / offset)

    # For pages below 1 will return Page 1
    page = max(page, 1)

    # For pages above total_pages will return Last Page
    page = min(page, total_pages)

    start = (page - 1) * offset
    end = min(start + offset, length)

    return (start, end)
