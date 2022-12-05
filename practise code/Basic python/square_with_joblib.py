import time
from math import sqrt
from joblib import Parallel, delayed



def f(i):
    num=10000
    pro=1
    for j in range(num):
        for k in range(j):
            pro*=k
    
    return sqrt (i**2)


rng= 10
start_time=time.time()

# for i in range(rng):
#     f(i)
job= Parallel(n_jobs=2)(delayed(f)(i) for i in range(rng))

end_time=time.time()
print(end_time-start_time)

#8.186060190200806