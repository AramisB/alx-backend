#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits
from BaseCaching and is a caching system:
"""

from collections import OrderedDict
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
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item into the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
