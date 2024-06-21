from collections import OrderedDict
from cache.eviction_policies import EvictionPolicyEnum


class InMemoryCache:
    def __init__(self, memory=5, eviction_policy=EvictionPolicyEnum.LRU):
        self.memory = memory
        self.cache = OrderedDict()
        self.eviction_policy = eviction_policy()

    def set(self, key, value):
        """Set a value in the cache."""

        if len(self.cache) >= self.memory:
            if key in self.cache:
                # Update key order if already present in cache
                if isinstance(self.eviction_policy, (EvictionPolicyEnum.LRU, EvictionPolicyEnum.MRU)):
                    self.cache.move_to_end(key)
            else:
                # Evict if cache is full when adding new keys
                self.eviction_policy.evict(self.cache)

        self.cache[key] = value

    def get(self, key):
        """Get a value from the cache. Return None if key is not present."""
        value = self.cache.get(key, None)

        if value is not None and isinstance(self.eviction_policy, (EvictionPolicyEnum.LRU, EvictionPolicyEnum.MRU)):
            # Update key order for recently used keys
            self.cache.move_to_end(key)

        return value

    def delete(self, key):
        """Delete a value from the cache by its key."""
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """Clear all values from the cache."""
        self.cache.clear()
