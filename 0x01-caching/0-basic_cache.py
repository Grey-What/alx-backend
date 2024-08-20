#!/usr/bin/env python3
"""
BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """basic cache class"""
    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """
        put for cache system

        Args:
            key: key of cache item in ditionary
            item: value of cache item in ditionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get for cache system for specific key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
