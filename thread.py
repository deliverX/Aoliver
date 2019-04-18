#!/usr/bin/python

import time
import threading

#继承Thread类，重写run()方法
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,lock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.lock = lock
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        self.lock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        self.lock.release()

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


def main():

    threadLock =threading.Lock()
    threads = []

    thread1 = myThread(1,"Thread-1",1,threadLock)
    thread2 = myThread(2,"Thread-2",2,threadLock)

    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)

    for t in threads:
        t.join()

    print ("退出主线程")

if __name__ == '__main__':
    main()
