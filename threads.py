# %%

import threading
from time import sleep

# %%

threading.active_count()  # 8

# %%

class MyThread(threading.Thread):

    def run(self):
        print("Run method in custom thread object invoked!")

t = MyThread()
t.start()  # calls run method in seperate thread

# %%

t = threading.Thread(target=lambda: print("Run method in thread object invoked!"))
t.start()  # calls run method in seperate thread

# %%

lock = threading.Lock()

lock.acquire()  # True
lock.acquire(timeout=1.0)  # False (due to timeout)
lock.locked()  # True (since lock still acquired)
lock.release()

# %%

rlock = threading.RLock()

rlock.acquire()  # True
rlock.acquire(timeout=1.0)  # True (since same thread (main) can aquire it multiple times; also increments recursion level)
rlock.release()
rlock.release()  # recursion level zero; can now be aquired by another thread

# %%

sem = threading.Semaphore(3)  # useful when size of resource is fixed e.g. num connections to database

sem.release()
sem._value  # 4
sem.acquire()  # True
sem.acquire()  # True
sem.acquire()  # True
sem.acquire()  # True
sem._value  # 0
sem.acquire(timeout=1.0)  # False (due to timeout)

# %%

sem = threading.BoundedSemaphore(3)

sem.release()  # error (released too many times)

# %%

event = threading.Event()

def countdown():
    for i in [3, 2, 1]:
        print(i)
        sleep(1.0)
    print("Go!")
    event.set()

def race():
    event.wait()
    print("Broom!")  # waits for countdown to set event flag

threading.Thread(target=countdown).start()
threading.Thread(target=race).start()

# %%
