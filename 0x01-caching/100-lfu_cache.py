#!/usr/bin/env python3
"""
Least Frequently Used caching system.
"""
from collections import defaultdict, OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """
        Initializes the cache.
        """
        super().__init__()
        self.cache_data = {}
        self.frequency = defaultdict(int)  # Tracks access frequency
        self.freq_order = defaultdict(OrderedDict)
        self.min_freq = 0  # Keeps track of the minimum frequency

    def __update_frequency(self, key):
        """
        Updates the frequency of the given key and reorders it.
        """
        current_freq = self.frequency[key]
        new_freq = current_freq + 1

        # Remove the key from the current frequency list
        del self.freq_order[current_freq][key]
        if not self.freq_order[current_freq]:
            if current_freq == self.min_freq:
                self.min_freq += 1
            del self.freq_order[current_freq]

        # Add the key to the new frequency list
        if new_freq not in self.freq_order:
            self.freq_order[new_freq] = OrderedDict()
        self.freq_order[new_freq][key] = self.cache_data[key]
        self.frequency[key] = new_freq

    def put(self, key, item):
        """
        Adds an item in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and its frequency
            self.cache_data[key] = item
            self.__update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict the least frequently used item
                lfu_key, _ = self.freq_order[self.min_freq].popitem(last=False)
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add the new item
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.freq_order[1][key] = item
            self.min_freq = 1

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency of the accessed key
        self.__update_frequency(key)
        return self.cache_data[key]
