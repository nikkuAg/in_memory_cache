from collections import OrderedDict

from cache.eviction_policies import EvictionPolicy


class MRUPolicy(EvictionPolicy):
    """Most Recently Used eviction policy."""

    def evict(self, cache: OrderedDict):
        """Evict the oldest entry in the cache."""
        cache.popitem(last=True)
