from collections import OrderedDict
from cache.eviction_policies import EvictionPolicy


class FIFOPolicy(EvictionPolicy):
    """First In First Out eviction policy."""

    def evict(self, cache: OrderedDict):
        """Evict the oldest entry in the cache."""
        cache.popitem(last=False)
