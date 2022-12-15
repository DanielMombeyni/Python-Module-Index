import _thread

def foo(arg):
    print(arg)

arg="hello"
_thread.start_new_thread(foo, (arg,))