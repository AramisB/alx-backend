#!/usr/bin/env python3
"""
simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    parameters: page and page_size
    return: tuple of size two
    """
    return ((page - 1) * page_size, page * page_size)
