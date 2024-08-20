#!/usr/bin/env python3
"""FIFO caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Init"""
        super().__init__()

    def put(self, key, item):
        """
        Put for caching system

        Args:
            key: key of cache item in ditionary
            item: value of cache item in ditionary
        """
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data):
            first = next(iter(self.cache_data))
            del self.cache_data[first]
            print("DISCARD: {}".format(first))

        self.cache_data[key] = item

    def get(self, key):
        """
        Get for caching system

        Args:
            key: key of cache item in ditionary
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
