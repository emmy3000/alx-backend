#!/usr/bin/env python3
"""
Hypermedia Pagination

This script defines a Server class for paginating a database
of popular baby names and provides a method to retrieve hypermedia
information for a specified page and page size.
"""
import csv
import math
from typing import List, Dict, Tuple


class Server:
    """
    Server class for paginating a database of popular baby names.
    This class provides methods to retrieve data and hypermedia information
    for a specified page and page size.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieves the dataset from the CSV file and caches it.

        Returns:
            List[List]: The dataset as a list of rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Calculate the start and end indexes for a given page and page size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Tuple[int, int]: A tuple (start_index, end_index) representing
            the range of indexes for the given pagination parameters.
        """
        if page < 1 or page_size < 1:
            raise ValueError("Both page and page_size must be +ve integers.")
        start = (page - 1) * page_size
        end = start + page_size
        return start, end

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The requested page of data from the dataset.
        """
        start, end = self.index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve hypermedia information about a page.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict: Information about the page, including page size, page number,
            data, next page, previous page, and total pages.
        """
        page_data = self.get_page(page, page_size)
        start, end = self.index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
