import time
import datetime
import random


requests = []


def get_time():
#    r = random.randrange(0, 10)
#    time.sleep(r)
    t = datetime.datetime.now()
    return t


if __name__ == '__main__':

    requests.append((get_time(), "123", "123"))
    requests.append((get_time(), "123", "123"))
    requests.append((get_time(), "123", "123"))
    requests.append((get_time(), "123", "123"))
    requests.append((get_time(), "123", "123"))
    requests.append((get_time(), "123", "123"))
    requests.append((get_time(), "123", "123"))

    print(requests[-1][0], requests[0][0])
    total_delta = (requests[-1][0] - requests[0][0])
    print("%d total request to go in %s time" % (len(requests), total_delta))

    last_time = requests[0][0]
    for r, s1, s2 in requests:
        delta = (r - last_time)
        if delta:
            if delta and delta.microseconds > 0:
                print('next req in %d sec ' % delta.seconds)
            time.sleep(delta.seconds)
        print(r)
        last_time = r