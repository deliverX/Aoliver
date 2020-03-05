#!/usr/bin/python

from multiprocessing import Process  
import os  
import time

def sleeper(name, seconds):  
    print("Process ID# %s" % (os.getpid()))  #获取当前进程ID
    print("Parent Process ID# %s" % (os.getppid())) #获取父进程ID
    print("%s will sleep for %s seconds" % (name, seconds))  
    time.sleep(seconds)
    
if __name__ == "__main__":  
  child_proc = Process(target = sleeper, args = ('bob', 5))  
  child_proc.start()  
  print("in parent process after child process start")  
  print("parent process about to join child process")
  child_proc.join()
  print("in parent process after child process join" ) 
  print("the parent's parent process: %s" % (os.getppid()))
