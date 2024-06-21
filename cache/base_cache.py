from collections import OrderedDict
from cache.eviction_policies import EvictionPolicyEnum
import time


class InMemoryCache:
    def __init__(self, memory=5, eviction_policy=EvictionPolicyEnum.LRU):
        self.memory = memory
        self.cache = OrderedDict()
        self.eviction_policy = eviction_policy()

    def set(self, key, value, ttl=None):
        """Set a value in the cache with an optional TTL (Time To Live)."""
        if ttl:
            expiry_time = time.time() + ttl
            value = (value, expiry_time)

        self.remove_expired_keys()

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
        """Get a value from the cache. Return None if the key is not found or expired."""
        value = self.cache.get(key, None)

        # Return None if the cache has expired
        if value and isinstance(value, tuple):
            value, expiry_time = value
            if time.time() >= expiry_time:
                del self.cache(key)
            return None

        # Update key order for recently used keys
        if value is not None and isinstance(self.eviction_policy, (EvictionPolicyEnum.LRU, EvictionPolicyEnum.MRU)):
            self.cache.move_to_end(key)

        return value

    def delete(self, key):
        """Delete a value from the cache by its key."""
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """Clear all values from the cache."""
        self.cache.clear()

    def remove_expired_keys(self):
        """Remove all expired values from the cache."""
        current_time = time.time()
        expired_keys = [key for key, value in self.cache.items(
        ) if isinstance(value, tuple) and value[1] < current_time]
        for key in expired_keys:
            del self.cache[key]
