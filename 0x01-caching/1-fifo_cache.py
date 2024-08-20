#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits
from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First-In First-Out caching system
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Add an item into the cache
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line
        """
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_order.remove(key)

        self.cache_data[key] = item
        self.cache_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key1 = self.cache_order.pop(0)
            del self.cache_data[key1]
            print(f"DISCARD: {key1}")

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
