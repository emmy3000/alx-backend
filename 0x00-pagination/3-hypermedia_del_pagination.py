#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This script defines a Server class for paginating a database
of popular baby names and provides a method to retrieve hypermedia
information for a specified page and page size.
"""
import csv
from typing import List, Dict


class Server:
    """
    Server class for paginating a database of popular baby names.
    This class provides methods to retrieve data and hypermedia information
    for a specified page and page size.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes a new Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieve the dataset from the CSV file and cache it.

        Returns:
            List[List]: The dataset as a list of rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create an indexed dataset for efficient pagination.

        Returns:
            Dict[int, List]: The dataset indexed by sorting position,
            starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i]
                for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve hypermedia information about a page based on the index.

        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: Information about the page, including index, next index,
            page size, and data.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        if index is None:
            index = 0
        next_index = index + page_size
        data = []
        for i in range(index, next_index):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])

        page_info = {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }

        return page_info
