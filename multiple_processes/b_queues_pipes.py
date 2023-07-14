from multiprocessing import Process, Queue, Pipe


#####################################################################
# Queue and Pip are for exchanging objects between processes
#####################################################################

def queue_func(q):
    q.put([42, None, "hello"])


def pip_func(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == "__main__":
    # Queues are thread and process safe.
    q = Queue()
    p = Process(target=queue_func, args=(q,))
    p.start()
    print q.get()
    p.join()

    # Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way).
    # two connection objects returned by Pipe() represent the two ends of the pipe. each object has send() and recv() methods (among others).
    parent_conn, child_conn = Pipe()  # type: (object, object)
    p1 = Process(target=pip_func, args=(child_conn,))
    p1.start()
    print parent_conn.recv()  # prints "[42, None, 'hello']"
    p1.join()
