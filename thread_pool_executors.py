# %%

from time import time, sleep
from concurrent.futures import ThreadPoolExecutor, as_completed

# %%

with ThreadPoolExecutor() as executor:
    future = executor.submit(pow, 2, 3)
    future.add_done_callback(lambda f: print(f.result()))

# %%

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(pow, 2, n) for n in [1, 2, "invalid input"]]

for future in as_completed(futures):
    try:
        print(future.result())
    except Exception as exc:
        print("Generated exception:", exc)

# %%

with ThreadPoolExecutor() as executor:
    for result in executor.map(lambda x: x ** 2, [1, 2, 3]):
        print(result)

# %%

start = time()
[sleep(1) for _ in range(3)]
print(f"Single threaded: completed in {time() - start:.2f} seconds")

start = time()
with ThreadPoolExecutor() as executor:
    executor.map(lambda _: sleep(1), range(3))  # executor.map is not lazy; lambda fn is called immediately
print(f"Multi-threaded: completed in {time() - start:.2f} seconds")

# %%
