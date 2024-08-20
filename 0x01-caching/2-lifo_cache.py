#!/usr/bin/env python3
"""LIFO caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """Init"""
        super().__init__()

    def put(self, key, item):
        """Put for caching system"""
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data):
            k, v = self.cache_data.popitem()
            print("DISCARD: {}".format(k))

        self.cache_data[key] = item

    def get(self, key):
        """Get for caching system"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
