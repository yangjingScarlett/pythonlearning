import multiprocessing
from multiprocessing import Process


# 1.Process class: One call of Process() function creates a new process
def f(name):
    print("hello " + name)


if __name__ == "__main__":
    # a simple sample to create a process to execute function f()
    p = Process(target=f, args=("Bob",))
    p.start()
    p.join()
