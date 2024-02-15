import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math


N=1000
y=np.array([0. for i in range(1000)])

for num in range(1000):
    data=np.array([[rand.randint(0,9) for i in range(N)]])
    y[num]=np.mean(data)

n,bins,patches=plt.hist(y,bins=20)

ave=np.mean(n)
print(ave)

sigma=np.std(n)/(N**1/2)
print(sigma)

plt.ylabel("number in the sample")
plt.show()