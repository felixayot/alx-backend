#!/usr/bin/python3
"""Module for FIFOCache class definition."""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Represents a fifo cache caching system.
    """
    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line
        """
        if key or item:
            self.cache_data.__setitem__(key, item)
        pass
        if len(self.cache_data) > __class__.MAX_ITEMS:
            (k := next(iter(self.cache_data)), self.cache_data.pop(k))
            print(f"DISCARD: {k}")

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        if key or key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
