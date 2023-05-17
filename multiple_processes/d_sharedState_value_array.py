from multiprocessing import Process, Value, Array, Manager


##############################################################
# Value and Array can share state, they are shared memory.
# object returned by Manager() controls a server process holds Python objects and allows other processes to manipulate them using proxies.
##############################################################

def shared_memory_func(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


def manager_func(d, l):
    d[1] = '1'
    d["2"] = 2
    d[0.25] = None
    l.reverse()


if __name__ == "__main__":
    num = Value('d', 0.0)  # 'd' means double
    arr = Array('i', range(10))  # 'i' means integer

    p = Process(target=shared_memory_func, args=(num, arr))
    p.start()
    p.join()
    print("************* Value and Array as shared memory *************")
    print(num.value)
    print(arr[:])

    manager = Manager()
    d = manager.dict()
    l = manager.list(range(10))
    p1 = Process(target=manager_func, args=(d, l))
    p1.start()
    p1.join()
    print("************* manager control server process *************")
    print(d)
    print(l)
