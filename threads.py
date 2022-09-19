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

with lock:
    print(lock.locked())  # True

lock.locked()  # False

# %%

rlock = threading.RLock()  # allows a thread to acquire the lock multiple times

rlock.acquire()  # True
rlock.acquire(timeout=1.0)  # True (since same thread (main) can aquire it multiple times; also increments recursion level)
rlock.release()
rlock.release()  # recursion level zero; can now be aquired by another thread

# %%

sem = threading.Semaphore(3)

sem.release()
sem._value  # 4
sem.acquire()  # True
sem.acquire()  # True
sem.acquire()  # True
sem.acquire()  # True
sem._value  # 0
sem.acquire(timeout=1.0)  # False (due to timeout)

# %%

sem = threading.BoundedSemaphore(3)  # useful when size of resource is fixed e.g. num connections to database

sem.release()  # error (released too many times)

# %%

event = threading.Event()  # allows communicatation between two threads

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

timer = threading.Timer(5.0, lambda: print("5 second timer up!"))
timer.start()  # Timer is a subclass of Thread; it's run method is invoked by calling start()

# %%

barrier = threading.Barrier(parties=2, timeout=5.0)  # a way to synchronise threads

def server():
    sleep(1.0)
    barrier.wait()
    # connection with client gauranteed here
    print("server: passed the barrier")

def client():
    sleep(2.0)
    barrier.wait()
    # connection with server gauranteed here
    print("client: passed the barrier")

threading.Thread(target=server).start()
threading.Thread(target=client).start()

# %%
