#!/usr/bin/env python3
"""
A basic caching module for storing and retrieving items.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Represents an object that allows the storage and retrieval
    of items from a dictionary.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: A unique identifier for the item.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: A unique identifier for the item.

        Returns:
            The item associated with the provided key if found;
            otherwise, None.
        """
        return self.cache_data.get(key, None)
