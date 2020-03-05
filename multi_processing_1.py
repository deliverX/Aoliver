#!/usr/bin/python
import multiprocessing as mp
def do(n) :
  #获取当前线程的名字
  name = mp.current_process().name
  print(name,'starting')
  print("worker ", n)
  return 

if __name__ == '__main__' :
  numList = []
  for i in range(8) :
    p = mp.Process(target=do, args=(i,))
    numList.append(p)
    p.start()#就绪状态
    #子进程执行完毕了才会执行主进程后面的语句。p进程通过join方法通知主进程死等我结束再继续执行。
    print("Process end.")
  for i in numList:
    i.join()#每个进程执行结束才会开始下一个循环
  print(numList)#5个进程全部执行完毕才执行print语句，也就是主进程死等
