import _thread

a_lock = _thread.allocate_lock()

with a_lock:
    print("a_lock is locked while this executes")