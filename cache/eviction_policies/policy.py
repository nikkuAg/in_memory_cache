from abc import ABC, abstractmethod
from collections import OrderedDict
from enum import Enum
from cache.eviction_policies import FIFOPolicy, LIFOPolicy, MRUPolicy, LRUPolicy


class EvictionPolicy(ABC):
    """Abstract base class for eviction policies."""

    @abstractmethod
    def evict(self, cache: OrderedDict):
        """Evict an entry from the cache."""
        pass


class EvictionPolicyEnum(Enum):
    FIFO = FIFOPolicy
    LIFO = LIFOPolicy
    LRU = LRUPolicy
    MRU = MRUPolicy
