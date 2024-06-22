from collections import OrderedDict

from cache.eviction_policies import EvictionPolicy


class LRUPolicy(EvictionPolicy):
    """Least Recently Used eviction policy."""

    def evict(self, cache: OrderedDict):
        """Evict the least recently used entry in the cache."""
        cache.popitem(last=False)
