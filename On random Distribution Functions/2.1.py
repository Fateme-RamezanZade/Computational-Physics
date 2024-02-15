import random as rand
import numpy as np
import matplotlib.pyplot as plt

N=100000
arr=np.array([rand.randint(0,9) for i in range(N)])
data=np.array([0])
counter=0
#print(arr)
for i in range(len(arr)-1):
    if arr[i+1]==4:
        data=np.append(data,0)
        data[counter]=arr[i]
        counter+=1
data=np.delete(data, len(data)-1)
print(counter)        
#print(data)
n,bins,patches=plt.hist(data, bins=range(11), align='left',edgecolor='black')
plt.ylabel("number in the sample")
#print(n)
plt.show()