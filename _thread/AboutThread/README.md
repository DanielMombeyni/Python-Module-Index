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
