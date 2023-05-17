#!/usr/bin/python3
"""
class LIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache"""
    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value
