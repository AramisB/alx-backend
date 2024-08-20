#!/usr/bin/env python3
"""
Create a class LRUCache that inherits
from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Least Recently Usef (LRU) caching system
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
        """
        if key is None and item is None:
            return
        if key in self.cache_data:
            self.cache_order.remove(key)

        elif len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.cache_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")
        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist
        in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
