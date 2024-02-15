import random as rand
import numpy as np
import matplotlib.pyplot as plt

N=10000
arr=np.array([rand.randint(0,9) for i in range(N)])
n,bins,patches=plt.hist(arr, bins=range(11), align='left',edgecolor='black')
print(n)
plt.ylabel("number in the sample")
plt.show()
