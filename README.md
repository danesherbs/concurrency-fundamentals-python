## Threading vs multiprocessing in Python

| Threads                                         | Processes                                           |
|-------------------------------------------------|-----------------------------------------------------|
| Spawned within existing process                 | New process created independent of existing process |
| Fast to spawn                                   | Slow to spawn                                       |
| Memory shared with other threads in the process | Memory not shared between processes                 |
| GIL shared with other threads in the process    | GIL not shared between processes (one per process)  |


## When to use one over the other

### Threads

Threading allows you to run code concurrently (but not in parallel). Threading is used to speed up programs which are I/O-bound (that is, when the program spends most of its time communicating). This can happen when making network requests or writing to a hard drive. Threading speeds up I/O-bound programs by overlapping the time spent waiting. 

### Processes

Multiprocessing allows you to run code in parallel. Multiprocessing is used to speed up programs which are CPU-bound (that is, when the program spends most of its time doing CPU operations). This can happen when doing computationally itensive tasks like using map reduce. Multiprocessing speeds up CPU-bound programs by doing more computations per second.

## Python threading and multiprocessing API

The Python API for both threads and processes is the same; they both have a `run()` method which is invoked when the thread's/processes `start()` method is invoked.
