import numpy as np
import math
import matplotlib.pyplot as plt
import random as rand

def p(x):
    sigma=1.
    return (2*math.pi*sigma)**(-0.5)*math.exp(-x**2/(2*sigma**2))
    

x=0
delta=7
N=10000
x_arr=np.array([x])

for n in range(N):
    i=np.random.uniform(-1,1)
    y=x+i*delta
    if p(x)>0:
        r=rand.random()
        if r<(p(y)/p(x)):
            x=y
            x_arr=np.append(x_arr,[x])
        
rate=len((x_arr)-1)/N
print(rate)
plt.hist(x_arr,bins=20,label='delta=%s, a.rate=%s'%(delta,rate))
plt.legend(loc='upper left')
plt.show()




