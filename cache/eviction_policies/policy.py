from abc import ABC, abstractmethod
from collections import OrderedDict


class EvictionPolicy(ABC):
    """Abstract base class for eviction policies."""

    @abstractmethod
    def evict(self, cache: OrderedDict):
        """Evict an entry from the cache."""
        pass
