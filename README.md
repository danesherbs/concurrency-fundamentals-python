## Threading vs multiprocessing in Python

| Threads                                         | Processes                                           |
|-------------------------------------------------|-----------------------------------------------------|
| Spawned within existing process                 | New process created independent of existing process |
| Fast to spawn                                   | Slow to spawn                                       |
| Memory shared with other threads in the process | Memory not shared between processes                 |
| GIL shared with other threads in the process    | GIL not shared between processes (one per process)  |
