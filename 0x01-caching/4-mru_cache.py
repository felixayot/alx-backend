#!/usr/bin/env python3
"""Module for MRUCache class definition."""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Represents a mru cache caching system.
    """
    def __init__(self):
        """Initializes an instance of a mru cache."""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS:
        you must discard the most recently used item
        in the cache (MRU algorithm)
        you must print DISCARD: with the key discarded
        followed by a new line.
        """
        if key or item:
            self.cache_data.__setitem__(key, item)
            if len(self.cache_data) > __class__.MAX_ITEMS:
                if self.stack:
                    mru_key = self.stack.pop()
                    self.cache_data.popitem()
                    print(f"DISCARD: {mru_key}")
            if key not in self.stack:
                self.stack.append(key)
            self.pop_last(key)
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

    def pop_last(self, element):
        """
        Removes and inserts cache_data's most recent accessed key
        in the cache system stack.
        """
        size = len(self.stack)
        if self.stack[size - 1] != element:
            self.stack.remove(element)
            self.stack.append(element)
