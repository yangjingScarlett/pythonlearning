from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    print("hello, ", i)
    l.release()


if __name__ == "__main__":
    lock = Lock()
    for i in range(10):
        p = Process(target=f, args=(lock, i))
        p.start()
        p.join()
