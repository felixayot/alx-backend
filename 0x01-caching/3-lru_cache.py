#!/usr/bin/env python3
"""Module for LRUCache class definition."""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Represents a lru cache caching system.
    """
    def __init__(self):
        """Initializes an instance of a lru cache."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LRU algorithm)
        you must print DISCARD: with the key discarded
        followed by a new line
                if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)
        """
        if key and item:
            self.cache_data.__setitem__(key, item)
            if len(self.queue) > __class__.MAX_ITEMS:
                lru_key = self.get_first_list(self.queue)
                if lru_key:
                    self.queue.pop(0)
                    self.cache_data.pop(lru_key)
                print(f"DISCARD: {lru_key}")
            if key not in self.queue:
                self.queue.append(key)
            else:
                self.list_move_last(key)
        pass

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        item = self.cache_data.get(key, None)
        if item is not None:
            self.list_move_last(key)
        return item

    def list_move_last(self, item):
        """
        Moves element to last index of a list.
        """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first_list(array):
        """
            Gets first element of list or None.
        """
        return array[0] if array else None
