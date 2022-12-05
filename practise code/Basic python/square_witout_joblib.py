import time
from math import sqrt




def f(i):
    num=10000
    pro=1
    for j in range(num):
        for k in range(j):
            pro*=k
    
    return sqrt (i**2)


rng= 10
start_time=time.time()

for i in range(rng):
    f(i)


end_time=time.time()
print(end_time-start_time)

#14.270013809204102