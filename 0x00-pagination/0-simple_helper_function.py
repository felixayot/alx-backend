#!/usr/bin/env python3
"""Script for index_range function."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    end = page * page_size
    start = end - page_size
    return start, end
