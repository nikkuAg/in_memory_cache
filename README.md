# In-Memory Cache with Eviction Policies

## Overview

This Python project implements a thread-safe, in-memory cache with configurable eviction policies. The cache allows storing key-value pairs and supports eviction strategies such as LRU (Least Recently Used), MRU (Most Recently Used), FIFO (First In, First Out), and LIFO (Last In, First Out). It's designed to manage memory efficiently in applications requiring fast access to frequently accessed data.

## Features

- **Thread-Safe**: Utilizes threading locks (`threading.Lock`) to ensure safe concurrent access.
- **Eviction Policies**: Supports multiple eviction policies:
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)
  - FIFO (First In, First Out)
  - LIFO (Last In, First Out)
- **Expiration**: Optional expiration time (TTL) for cached items.
- **Clearing and Deleting**: Methods to clear the entire cache or delete specific items.
- **Extensible Design**: Easily extendable to support additional eviction policies or customization.

## Installation

1. **Clone the Repository**:

Fork the repository on GitHub first, then clone your fork

```bash
git clone https://github.com/<your-github-username>/in_memory_cache.git
cd in_memory_cache
```

2. **Create virtual environment**:

```python
python -m venv env
```

3. **Activate virtual environment**:

```bash
source env/bin/activate
```

4. **Install Depedencies**:

```bash
pip install -r requirements.txt
```

## Usage

**Example Code**

```python
from cache.base_cache import InMemoryCache
from cache.eviction_policies import EvictionPolicyEnum

# Initialize the cache with LRU eviction policy
cache = InMemoryCache(capacity=100, eviction_policy=EvictionPolicyEnum.LRU)

# Set values in the cache
cache.set('key1', 'value1')
cache.set('key2', 'value2', ttl=60)  # with TTL of 60 seconds

# Retrieve values from the cache
value1 = cache.get('key1')
value2 = cache.get('key2')

# Delete a value from the cache
cache.delete('key1')

# Clear the cache
cache.clear()
```

**Eviction Policies**

```python
from cache.eviction_policies import EvictionPolicyEnum

# Example with MRU eviction policy
cache.set_eviction_policy(EvictionPolicyEnum.MRU)
```

**Thread Safety**

```python
import threading

# Example using threads
def worker():
    cache.set('key', 'value')

threads = []
for _ in range(10):
    thread = threading.Thread(target=worker)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Ensure cache consistency after threads complete
assert len(cache.cache) <= 3, "Cache should not have more than 3 items."
```
