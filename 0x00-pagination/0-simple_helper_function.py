#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    helper function that return a tuple of size two containing
    a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters

    Args:
        page (int): the current page
        page_size (int): the size of the current page

    Returns:
        tuple: start index and end index
    """
    return ((page - 1) * page_size, page * page_size)
