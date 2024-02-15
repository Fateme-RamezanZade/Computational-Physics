import numpy as np
import math
import matplotlib.pyplot as plt
import random as rand

def p(x):
    sigma=1.
    return (2*math.pi*sigma)**(-0.5)*math.exp(-x**2/(2.*sigma**2))


N=10000
accept=np.array([0. for i in range(200)])
for k in range(200):
    delta=0.1*(k+1)
    x=0
    x_arr=np.array([x])
    for n in range(N):
        j=rand.random()
        if j<0.5:
            i=1.
        else:
            i=-1.
        i=np.random.uniform(-1,1)
        y=x+i*delta
        if p(x)>0:
            r=rand.random()
            if r<(p(y)/p(x)):
                x=y
                x_arr=np.append(x_arr,[x]) 
    rate=(len(x_arr)-1)/N
    accept[k]=rate

for i in range(len(accept)):
    print('delta=%s'%(0.1*(i+1)))
    print('rate=%s'%accept[i])
    plt.plot(0.1*(i+1),accept[i],'ro')

plt.xlabel('delta')
plt.ylabel('acceptance rate')

plt.show()





