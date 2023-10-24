#!/usr/bin/env python3

"""
Pagination and Dataset Pagination

This script defines a function for calculating start and end indexes for a
given pagination scenario. It also provides a Server class for paginating
a database of popular baby names and retrieving pages of data from the dataset.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    This function takes two integer arguments: page and page_size. It returns
    a tuple containing the start and end indexes for the range of elements
    to be displayed on a particular page.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple (start_index, end_index) that reps the range
        of indexes to return in a list for the given pagination parameters.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The requested page of data from the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index <= len(dataset):
            return dataset[start_index:end_index]
        else:
            return []
