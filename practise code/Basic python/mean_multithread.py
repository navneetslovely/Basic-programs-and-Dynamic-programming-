from multiprocessing import Process, Queue
import math
import numpy as np
import time

n=100000000
d=np.random.rand(n)


def mean_MP(s,e,q):
    sum=0
    for i in range(s, e+1):
        sum+=d[i]


    mean =sum/(e-s+1)
    q.put(mean)
    return 

n1=math.floor(n/2)
q=Queue()
if __name__=='__main__':     ## without __name__=='__main__' code will not work porperly
    p1=Process(target=mean_MP,args=(0,n1,q))
    p2=Process(target=mean_MP,args=(n1+1,n-1,q))


    start_time=time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    m=0

    while not q.empty():
        m+=q.get()

    m/=2

    end_time=time.time()

    print(end_time-start_time)

    print(m)

