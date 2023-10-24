#!/usr/bin/env python3
"""
Pagination Index Calculator

This script defines a function for calculating start and end indexes for a
given pagination scenario. It also provides an example of how to use the
function.
"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for a given page and page size.

    This function takes two integer arguments: page and page_size. It returns
    a tuple containing the start and end indexes for the range of elements
    to be displayed on a particular page.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple (start_index, end_index) representing the range
        of indexes to return in a list for the given pagination parameters.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size must be positive integers.")

    start_index = (page - 1) * page_size + 1
    end_index = page * page_size
    return start_index, end_index
