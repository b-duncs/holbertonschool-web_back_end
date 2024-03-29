#!/usr/bin/python3
"""
class LRUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache document"""
    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """
        must discard the least recently used item (LRU algorithm)
        """
        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        """
        must discard the least recently used item (LRU algorithm)
        """
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        """
        must print DISCARD: with the key discarded
        and following by a new line
        """
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self._remove(self.next[self.head])

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key
        """
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            self._remove(key)
            self._add(key, value)
            return value
