import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math

N=1000
x=np.array([0. for i in range(N)])
y=np.array([0. for i in range(N)])
for i in range(N):
    y1=rand.random()
    y2=rand.random()
    sigma=2
    theta=(2*math.pi)*y2
    rho=(-2*sigma*math.log(1-y1))**(1/2)
    x[i]=rho*math.cos(theta)
    y[i]=rho*math.sin(theta)
plt.plot(x,y,'ro')
plt.xlabel("x=rcos(theta)")
plt.ylabel("y=rsin(theta)")
plt.show()
n,bins,patches=plt.hist(x, bins=30,edgecolor='black')
n,bins=np.histogram(x, bins=30)
plt.ylabel("number in the sample x")
plt.show()
n,bins,patches=plt.hist(y, bins=30,edgecolor='black')
n,bins=np.histogram(y, bins=30)
plt.ylabel("number in the sample y")
plt.show()
plt.show()