## Threading vs multiprocessing in Python

| Threads                                         | Processes                                           |
|-------------------------------------------------|-----------------------------------------------------|
| Spawned within existing process                 | New process created independent of existing process |
| Fast to spawn                                   | Slow to spawn                                       |
| Memory shared with other threads in the process | Memory not shared between processes                 |
| GIL shared with other threads in the process    | GIL not shared between processes (one per process)  |


## When to use one over the other

Threading enables you to run code concurrently but not in parallel. Threading is used to speed up programs which are I/O bound (e.g. lots of accessing the file system or making network requests).

Multiprocessing enables you to run code in parallel. Multiprocessing is used to speed up programs which are _not_ I/O bound (e.g. using map reduce to sum up a large array of integers).

## Python threading and multiprocessing API

The Python API for both threads and processes is the same; they both have a `run()` method which is invoked when the thread/processes `start()` method is invoked.