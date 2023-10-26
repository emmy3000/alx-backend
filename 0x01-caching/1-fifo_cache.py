#!/usr/bin/env python3
"""
A First-In First-Out (FIFO) caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Represents an object for storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """
        Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key: A unique identifier for the item.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Retrieves an item by key.

        Args:
            key: A unique identifier for the item.

        Returns:
            The item associated with the provided key if found;
            otherwise, None.
        """
        return self.cache_data.get(key, None)
