#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits
from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Last-In First-Out caching system
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item into the cache
        """
        if key is None and item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            if self.last_key is not None:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")
        self.last_key = key

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
