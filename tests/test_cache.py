import threading
import time
import unittest

from cache.base_cache import InMemoryCache
from cache.eviction_policies import EvictionPolicyEnum


class TestCache(unittest.TestCase):
    """Unit tests for the BaseCache class and eviction policies."""

    def test_fifo_eviction(self):
        cache = InMemoryCache(memory=3, eviction_policy=EvictionPolicyEnum.FIFO)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        cache.set("d", 4)  # This should evict 'a'
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("b"), 2)

    def test_lru_eviction(self):
        cache = InMemoryCache(memory=3, eviction_policy=EvictionPolicyEnum.LRU)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        cache.get("a")  # Access 'a' to mark it as recently used
        cache.set("d", 4)  # This should evict 'b'
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)

    def test_mru_eviction(self):
        cache = InMemoryCache(memory=3, eviction_policy=EvictionPolicyEnum.MRU)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        cache.get("a")  # Access 'a' to mark it as recently used
        cache.set("d", 4)  # This should evict 'a'
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("b"), 2)

    def test_lifo_eviction(self):
        cache = InMemoryCache(memory=3, eviction_policy=EvictionPolicyEnum.LIFO)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        cache.set("d", 4)  # This should evict 'c'
        self.assertIsNone(cache.get("c"))
        self.assertEqual(cache.get("d"), 4)

    def test_ttl_expiry(self):
        cache = InMemoryCache(memory=3)
        cache.set("a", 1, ttl=1)  # Set 'a' with a TTL of 1 second
        time.sleep(1.5)  # Wait for 'a' to expire
        self.assertIsNone(cache.get("a"))

    def test_remove_expired_keys(self):
        cache = InMemoryCache(memory=3)
        cache.set("a", 1, ttl=1)  # Set 'a' with a TTL of 1 second
        cache.set("b", 2, ttl=2)  # Set 'b' with a TTL of 2 seconds
        cache.set("c", 3, ttl=3)  # Set 'a' with a TTL of 1 second
        time.sleep(2.5)  # Wait for 'a' and 'b' to expire
        cache.remove_expired_keys()  # Remove expired keys
        self.assertIsNone(cache.get("a"))
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("c"), 3)

    def test_clear_cache(self):
        cache = InMemoryCache(memory=3)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        cache.clear()
        self.assertIsNone(cache.get("a"))
        self.assertIsNone(cache.get("b"))
        self.assertIsNone(cache.get("c"))
        self.assertEqual(len(cache.cache), 0)

    def test_delete_key(self):
        cache = InMemoryCache(memory=3)
        cache.set("a", 1)
        cache.delete("a")
        self.assertIsNone(cache.get("a"))

    def test_set_eviction_policy(self):
        cache = InMemoryCache(memory=3)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)
        cache.get("b")
        cache.set_eviction_policy(EvictionPolicyEnum.MRU)
        # This should evict 'b' if policy is correctly updated
        cache.set("d", 4)
        self.assertIsNone(cache.get("b"))

    def test_thread_safety(self):
        cache = InMemoryCache(memory=3)

        def add_items():
            for i in range(1000):
                cache.set(f"key_{i}", i)

        threads = [threading.Thread(target=add_items) for _ in range(10)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # Cache should have 3 items, after all threads complete
        self.assertTrue(len(cache.cache) <= 3)


if __name__ == "__main__":
    unittest.main()
