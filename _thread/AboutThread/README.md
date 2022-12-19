# What is a Thread in Python

A thread is the execution of code in a Python process. Each program has one thread by default, but we may need to create new threads to execute tasks concurrently.

In this tutorial you will discover what a thread is in Python.

Let’s get started.

Skip the tutorial. Master threading today. [Learn how](https://superfastpython.com/threading-in-python/)

## What is a Thread

 thread refers to a thread of execution in a computer program.

Each program is a process and has at least one thread that executes instructions for that process.

> Thread: The operating system object that executes the instructions of a process.
    — Page 273, The Art of Concurrency, 2009.

When we run a Python script, it starts an instance of the Python interpreter that runs our code in the main thread. The main thread is the default thread of a Python process.

We may develop our program to perform tasks concurrently, in which case we may need to create and run new threads. These will be concurrent threads of execution without our program, such as:

- Executing function calls concurrently.
- Executing object methods concurrently.

A Python thread is an object representation of a native thread provided by the underlying operating system.

When we create and run a new thread, Python will make system calls on the underlying operating system and request a new thread be created and to start running the new thread.

This highlights that Python threads are real threads, as opposed to simulated software threads, e.g. fibers or green threads.

The code in new threads may or may not be executed in parallel (at the same time), even though the threads are executed concurrently.

There are a number of reasons for this, such as:

- The underlying hardware may or may not support parallel execution (e.g. one vs multiple CPU cores).
- The Python interpreter may or may not permit multiple threads to execute in parallel.

This highlights the distinction between code that can run out of order (concurrent) from the capability to execute simultaneously (parallel).

- Concurrent: Code that can be executed out of order.
- Parallel: Capability to execute code simultaneously.

You can learn more about Python threads in the guide:

- [Threading in Python: The Complete Guide](https://superfastpython.com/threading-in-python/)

Next, let’s consider the important differences between threads and processes.

Run your loops using all CPUs, [download my FREE book](https://superfastpython.com/plip-incontent) to learn how.

## Thread vs Process

A process refers to a computer program.

Each process is in fact one instance of the Python interpreter that executes Python instructions (Python byte-code), which is a slightly lower level than the code you type into your Python program.

> Process: The operating system’s spawned and controlled entity that encapsulates an executing application. A process has two main functions. The first is to act as the resource holder for the application, and the second is to execute the instructions of the application.
> — Page 271, [The Art of Concurrency](https://amzn.to/3z1XhOz), 2009.

The underlying operating system controls how new processes are created. On some systems, that may require spawning a new process, and on others, it may require that the process is forked. The operating-specific method used for creating new processes in Python is not something we need to worry about as it is managed by your installed Python interpreter.

A thread always exists within a process and represents the manner in which instructions or code is executed.

A process will have at least one thread, called the main thread. Any additional threads that we create within the process will belong to that process.

The Python process will terminate once all (non background threads) are terminated.

- Process: An instance of the Python interpreter has at least one thread called the MainThread.
- Thread: A thread of execution within a Python process, such as the MainThread or a new thread.

Now that we are clear on the differences between processes and threads, let’s take a look at the limitations of threads in Python.

Confused by the threading module API?
Download my FREE [PDF cheat sheet](https://marvelous-writer-6152.ck.page/088fc51f28)

## Limitations of Threads in Python

The reference Python interpreter is referred to as CPython.

It is the free version of Python that you can download from python.org to develop and run Python programs.

The CPython Python interpreter generally does not permit more than one thread to run at a time.

This is achieved through a mutual exclusion (mutex) lock within the interpreter that ensures that only one thread at a time can execute Python bytecodes in the Python virtual machine.

> In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation).
> [— threading — Thread-based parallelism](https://docs.python.org/3/library/threading.html)

This lock is referred to as the [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) or GIL for short.

> In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. The GIL prevents race conditions and ensures thread safety.
> [— Global Interpreter Lock, Python Wiki.](https://wiki.python.org/moin/GlobalInterpreterLock)

This means that although we might write concurrent code with threads in Python and run our code on hardware with many CPU cores, we may not be able to execute our code in parallel.

There are some exceptions to this.

Specifically, the GIL is released by the Python interpreter sometimes to allow other threads to run.

Such as when the thread is blocked, such as performing IO with a socket or file, or often if the thread is executing computationally intensive code in a C library, like hashing bytes.

>Luckily, many potentially blocking or long-running operations, such as I/O, image processing, and NumPy number crunching, happen outside the GIL. Therefore it is only in multithreaded programs that spend a lot of time inside the GIL, interpreting CPython bytecode, that the GIL becomes a bottleneck.
>[— Global Interpreter Lock, Python Wiki.](https://wiki.python.org/moin/GlobalInterpreterLock)

Therefore, although in most cases CPython will prevent parallel execution of threads, it is allowed in some circumstances. These circumstances represent the base use case for adopting threads in your Python programs.

Next, let’s look at specific cases when you should consider using threads

## When to Use a Thread

The reference Python interpreter CPython prevents more than one thread from executing bytecode at the same time.

This is achieved using a mutex called the Global Interpreter Lock or GIL, as we learned in the previous section.

There are times when the lock is released by the interpreter and we can achieve parallel execution of our concurrent code in Python.

Examples of when the lock is released include:

- When a thread is performing blocking IO.
- When a thread is executing C code and explicitly releases the lock.

There are also ways of avoiding the lock entirely, such has:

- Using a third-party Python interpreter to execute Python code.

Let’s take a look at each of these use cases in turn.

## Blocking IO

You should use threads for IO-bound tasks.

An IO-bound task is a type of task that involves reading from or writing to a device, file, or socket connection.

The operations involve input and output (IO), and the speed of these operations is bound by the device, hard drive, or network connection. This is why these tasks are referred to as IO-bound.

CPUs are really fast. Modern CPUs, like a 4GHz CPU, can execute 4 billion instructions per second, and you likely have more than one CPU core in your system.

Doing IO is very slow compared to the speed of CPUs.

Interacting with devices, reading and writing files and socket connections involves calling instructions in your operating system (the kernel), which will wait for the operation to complete. If this operation is the main focus for your CPU, such as executing in the main thread of your Python program, then your CPU is going to wait many milliseconds or even many seconds doing nothing.

That is potentially billions of operations prevented from executing.

A thread performing an IO operation will block for the duration of the operation. While blocked, this signals to the operating system that a thread can be suspended and another thread can execute, called a context switch.

Additionally, the Python interpreter will release the GIL when performing blocking IO operations, allowing other threads within the Python process to execute.

Therefore, blocking IO provides an excellent use case for using threads in Python.

Examples of blocking IO operations include:

- Reading or writing a file from the hard drive.
- Reading or writing to standard output, input or error (stdin, stdout, stderr).
- Printing a document.
- Reading or writing bytes on a socket connection with a server.
- Downloading or uploading a file.
- Querying a server.
- Querying a database.
- Taking a photo or recording a video.
- And so much more.

## External `C` Code

We may make function calls that themselves call down into a third-party C library.

Often these function calls will release the GIL as the C library being called will not interact with the Python interpreter.

This provides an opportunity for other threads in the Python process to run.

For example, when using the “hash” module in the Python standard library, the GIL is released when hashing the data via the [`hash.update()`function](https://docs.python.org/3/library/hashlib.html#hashlib.hash.update).

> The Python GIL is released to allow other threads to run while hash updates on data larger than 2047 bytes is taking place when using hash algorithms supplied by OpenSSL.
> [— hashlib — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)

Another example is the NumPy library for managing arrays of data which will release the GIL when performing functions on arrays.

> The exceptions are few but important: while a thread is waiting for IO (for you to type something, say, or for something to come in the network) python releases the GIL so other threads can run. And, more importantly for us, while numpy is doing an array operation, python also releases the GIL.
> [— Write multithreaded or multiprocess code, SciPy Cookbook.](https://scipy-cookbook.readthedocs.io/items/ParallelProgramming.html)

## Third-Party Python Interpreters

Another important consideration is the use of third-party Python interpreters.

There are alternate commercial and open source Python interpreters that you can acquire and use to execute your Python code.

Some of these interpreters may implement a GIL and release it more or less than CPython. Other interpreters remove the GIL entirely and allow multiple Python concurrent threads to execute in parallel.

Examples of third-party Python interpreters without a GIL include:

- Jython: an open source Python interpreter written in Java.
- IronPython: an open source Python interpreter written in .NET.

> … Jython does not have the straightjacket of the GIL. This is because all Python threads are mapped to Java threads and use standard Java garbage collection support (the main reason for the GIL in CPython is because of the reference counting GC system). The important ramification here is that you can use threads for compute-intensive tasks that are written in Python.
> [— No Global Interpreter Lock, Definitive Guide to Jython.](https://jython.readthedocs.io/en/latest/Concurrency/)

Next, let’s look at how to create new threads in Python.

## How to Create a New Thread

Sometimes, we may need to create additional threads within our Python process to execute tasks concurrently.

Python provides real native (system-level) threads via the threading.Thread class.

There two main ways to create a new thread, they are:

- Create a threading.Thread instance and configure it to run a function.
- Extend the threading.Thread class and override the run() function.

Let’s take a closer look at each approach.

### Example of Running a Function in a Thread

We can run a custom function in new threads.

This can be achieved by creating an instance of the **threading.Thread** class and specifying the function to run in the new thread via the target argument.

```python
# create and configure a new thread to run a function
thread = Thread(target=task)
```

Once the thread is created, it must be started by calling the **start()** function.

This function does not block and will return immediately, allowing the calling thread to continue on and execute other code.

We can then wait around for the task to complete by joining the thread, for example

```python
# wait for the task to complete
thread.join()
```

We can demonstrate this with a complete example with a task that sleeps for a moment and prints a message.

The complete example of executing a target task function in a separate thread is listed below.

```python
# SuperFastPython.com
# example of executing a target task function in a separate thread
from time import sleep
from threading import Thread
 
# a simple task that blocks for a moment and prints a message
def task():
    # block for a moment
    sleep(1)
    # display a message
    print('This is coming from another thread')
 
# create and configure a new thread to run a function
thread = Thread(target=task)
# start the task in a new thread
thread.start()
# display a message
print('Waiting for the new thread to finish...')
# wait for the task to complete
thread.join()
```

Running the example creates the thread object to run the **task()** function.

The thread is started and the **task()** function is executed in another thread. The task sleeps for a moment; meanwhile, in the main thread, a message is printed that we are waiting around and the main thread joins the new thread.

Finally, the new thread finishes sleeping, prints a message, and closes. The main thread then carries on and also closes as there are no more instructions to execute.

```md
Waiting for the new thread to finish...
This is coming from another thread
```

You can learn more about running a function in a new thread in this tutorial:

- [How to Run a Function in a New Thread in Python](https://superfastpython.com/run-function-in-new-thread/)

## Example of Extending the Thread Class

The **threading.Thread** class can be extended to run code in another thread.

This can be achieved by first extending the class, just like any other Python class.

For example:

```python
# custom thread class
class CustomThread(Thread):
    # ...
```

Then the **run()** function of the **threading.Thread** class must be overridden to contain the code that you wish to execute in another thread.

In this case, we will block for a moment and then print a message.

```python
# override the run function
def run(self):
    # block for a moment
    sleep(1)
    # display a message
    print('This is coming from another thread')
```

We can create an instance of our **CustomThread** class and call the **start()** function to begin executing our **run()** function in another thread. Internally, the **start()** function will call the **run()** function.

The code will then run in a new thread as soon as the operating system can schedule it.

```python
# create the thread
thread = CustomThread()
# start the thread
thread.start()
```

Finally, we wait for the new thread to finish executing.

```python
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
```

Tying this together, the complete example of executing code in another thread by extending the **threading.Thread** class is listed below.

```python
# SuperFastPython.com
# example of extending the Thread class
from time import sleep
from threading import Thread
 
# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        print('This is coming from another thread')
 
# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
```

Running the example first creates an instance of the thread, then executes the content of the **run()** function.

Meanwhile, the main thread waits for the new thread to finish its execution, before exiting.

You can learn more about how to extend the threading.Thread class in this tutorial:

- [How to Extend the Thread Class in Python](https://superfastpython.com/extend-thread-class/)

Further Reading

This section provides additional resources that you may find helpful.

Books

- [Python Threading Jump-Start](https://amzn.to/3O4XOop), Jason Brownlee, 2022 (my book!).
- [Threading API Interview Questions](https://amzn.to/3Adz73E)
- [Threading Module API Cheat Sheet](https://superfastpython.gumroad.com/l/rszuok)

I also recommend specific chapters in the following books:

- [Python Cookbook](https://amzn.to/3MSFzBv), David Beazley and Brian Jones, 2013.
        See: Chapter 12: Concurrency
- [Effective Python](https://amzn.to/3GpopJ1), Brett Slatkin, 2019.
        See: Chapter 7: Concurrency and Parallelism
- [Python in a Nutshell](https://amzn.to/3m7SLGD), Alex Martelli, et al., 2017.
        See: Chapter: 14: Threads and Processes

**Guides**

- [Python Threading: The Complete Guide](https://superfastpython.com/threading-in-python/)

**APIs**

- [threading - Thread-based parallelism](https://docs.python.org/3/library/threading.html)

[Reference](https://superfastpython.com/what-is-a-thread-in-python/)
