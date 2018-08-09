import time
import datetime
import random
from threading import Thread, Lock

LOCK = Lock()

requests = []


def secure_print(s1):
    LOCK.acquire()
    print(s1)
    LOCK.release()


def get_time():
    r = random.randrange(0, 2)
    time.sleep(r)
    t = datetime.datetime.now()
    return t


def b(b_list):
    for i in range(1, 5):
        b_list.append((get_time(), "B", "1"))

    time.sleep(1)
    print("processing b ...")

    total_delta = (b_list[-1][0] - b_list[0][0])
    print("%d total request to go in %s time" % (len(b_list), total_delta))

    last_time = b_list[0][0]
    for r, s1, s2 in b_list:
        delta = (r - last_time)
        if delta:
            print('next req in %f sec ' % (delta.total_seconds()))
            time.sleep(delta.total_seconds())
        print(str(datetime.datetime.now()) + ', ' + str(r) + ", " + s1)
        last_time = r


def reuters(r_list):
    for i in range(1, 5):
        r_list.append((get_time(), "R", "1"))

    time.sleep(10)
    print("processing reuters ...")

    total_delta = (r_list[-1][0] - r_list[0][0])
    print("%d total request to go in %s time" % (len(r_list), total_delta))

    last_time = r_list[0][0]
    for r, s1, s2 in r_list:
        delta = (r - last_time)
        secure_print(delta.total_seconds() * 1000)
        if delta:
            if delta and delta.seconds > 0:
                print('next req in %d sec ' % delta.seconds)
            time.sleep(delta.seconds)
        secure_print(str(r) + ", " + s1)
        last_time = r


if __name__ == '__main__':

    b_list = []
    r_list = []

    b_thread = Thread(target=b, args=(b_list,))
    r_thread = Thread(target=reuters, args=(r_list,))

    b_thread.start()
#    r_thread.start()

    b_thread.join()
#    r_thread.join()
    print("DONE !!")
