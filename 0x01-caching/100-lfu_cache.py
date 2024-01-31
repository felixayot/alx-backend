#!/usr/bin/python3
"""Module for LFUCache class definition."""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Represents a lfu cache caching system.
    """
    def __init__(self):
        """Initializes an instance of a lfu cache."""
        super().__init__()
        self.queue = []
        self.counter = {}

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS:
        you must discard the least frequently used item
        in the cache (LFU algorithm)
        you must print DISCARD: with the key discarded
        followed by a new line.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        item_count = self.counter.get(key, None)

        if item_count is not None:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                del self.counter[first]
                print("DISCARD: {}".format(first))

        if key not in self.queue:
            self.queue.insert(0, key)
        self.list_move_right(key)

    def get(self, key):
        """
            Returns the value in self.cache_data linked to key.
            If key is None or if the key doesn't exist in self.cache_data,
            return None.
        """
        item = self.cache_data.get(key, None)
        if item:
            self.counter[key] += 1
            self.list_move_right(key)
        return item

    def list_move_right(self, item):
        """
            Implements LFU by moving an element to the right.
        """
        length = len(self.queue)

        idx = self.queue.index(item)
        item_count = self.counter[item]

        for i in range(idx, length):
            if i != (length - 1):
                nxt = self.queue[i + 1]
                nxt_count = self.counter[nxt]

                if nxt_count > item_count:
                    break

        self.queue.insert(i + 1, item)
        self.queue.remove(item)

    @staticmethod
    def get_first_list(array):
        """
            Gets first element of list or None.
        """
        return array[0] if array else None
