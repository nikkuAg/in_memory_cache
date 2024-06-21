from collections import OrderedDict


class InMemoryCache:
    def __init__(self, memory=5):
        self.memory = memory
        self.cache = OrderedDict()

    def set(self, key, value):
        """Set a value in the cache."""
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value

    def get(self, key):
        """Get a value from the cache. Return None if key is not present."""
        value = self.cache.get(key, None)
        return value

    def delete(self, key):
        """Delete a value from the cache by its key."""
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """Clear all values from the cache."""
        self.cache.clear()
