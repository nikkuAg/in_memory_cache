from collections import OrderedDict

from cache.eviction_policies import EvictionPolicy


class LIFOPolicy(EvictionPolicy):
    """Last In First Out eviction policy."""

    def evict(self, cache: OrderedDict):
        """Evict the lastest added entry in the cache."""
        cache.popitem(last=True)
