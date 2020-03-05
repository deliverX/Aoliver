#!/usr/bin/python
import multiprocessing
import time 
def m1(x):
    time.sleep(0.05)
    return x

if __name__ == '__main__':
    print (multiprocessing.cpu_count())
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    i_list = ['h','i','j','k']
    time1=time.time()
    pool.map(m1, i_list)
    time2=time.time()
    print('time elapse:',time2-time1)

    time1=time.time()
    aoli = list(map(m1, i_list))
    print (aoli)
    time2=time.time()
    print('time elapse:',time2-time1)
