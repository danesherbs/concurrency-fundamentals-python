| Threads                                         | Processes                                          |
|-------------------------------------------------|----------------------------------------------------|
| Spawned within existing process                 | Spawned independent of existing process            |
| Fast                                            | Slow                                               |
| Memory shared with other threads in the process | Memory not shared between processes                |
| GIL shared with other threads in the process    | GIL not shared between processes (one per process) |