#!/usr/bin/env python3
"""LRU caching system"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""
    def __init__(self):
        """Init"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Put for caching system"""
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in
                self.cache_data):
            k, v = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(k))

        """if key is already in the cache, move it to the end"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

    def get(self, key):
        """Get for caching system"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
