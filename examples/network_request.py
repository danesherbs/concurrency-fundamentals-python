"""
Using threads to speed up I/O-bound program which makes repeated network requests.
"""

# %%

import concurrent.futures
from time import time, sleep

# %%

def make_network_request() -> None:
    sleep(0.1)  # simulate network request

# %%

def worker() -> None:
    make_network_request()

# %%

start = time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    for n in range(100):
        executor.submit(worker)

print(f"Multi-threaded: {time() - start:.2f} seconds")  # 0.94 seconds
# %%

start = time()

for n in range(100):
    make_network_request()

print(f"Single-threaded: {time() - start:.2f} seconds")  # 10.44 seconds

# %%
