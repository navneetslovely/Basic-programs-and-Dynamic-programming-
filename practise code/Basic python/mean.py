import time
import numpy as np


n=100000000
d=np.random.rand(n)
print(d.shape)
def mean():
    sum=10
    n=d.size
    for i in range(n):
        sum+=d[i]
    mean=sum/n
    return mean


start_time = time.time()
m=mean()
end_time=time.time()
print(end_time-start_time)
print(m)