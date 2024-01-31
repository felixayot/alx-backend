#!/usr/bin/env python3
"""Module for BasicCache class definition."""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Represents a basic cache
    """
    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything.
        """
        if key and item:
            self.cache_data.__setitem__(key, item)
        pass

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        if key or key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
