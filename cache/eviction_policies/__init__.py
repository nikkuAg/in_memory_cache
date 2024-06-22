from enum import Enum

from cache.eviction_policies.fifo import FIFOPolicy
from cache.eviction_policies.lifo import LIFOPolicy
from cache.eviction_policies.lru import LRUPolicy
from cache.eviction_policies.mru import MRUPolicy
from cache.eviction_policies.policy import EvictionPolicy


class EvictionPolicyEnum(Enum):
    FIFO = FIFOPolicy
    LIFO = LIFOPolicy
    LRU = LRUPolicy
    MRU = MRUPolicy
