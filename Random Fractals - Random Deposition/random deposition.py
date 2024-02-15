import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math

def mean(h):
    sum=0
    for i in range(len(h)):
        sum=sum+h[i]
    return sum/200
def dev(h):
    a=math.sqrt(mean(np.multiply(h,h))-mean(h)*mean(h))
    return a

h=np.array([[0] for x in range(200)])
for x in range(8000):
    i=rand.randint(0,199)
    h[i]=h[i]+1
h1=h.copy()
print(mean(h1.copy()))
print(dev(h1.copy()))
for x in range(8000):
    i=rand.randint(0,199)
    h[i]=h[i]+1
h2=h.copy()
print(mean(h2.copy()))
print(dev(h2.copy()))
for x in range(8000):
    i=rand.randint(0,199)
    h[i]=h[i]+1
h3=h.copy()
print(mean(h3.copy()))
print(dev(h3.copy()))
for x in range(8000):
    i=rand.randint(0,199)
    h[i]=h[i]+1
h4=h.copy()
print(mean(h4.copy()))
print(dev(h4.copy()))

for i in range(200):
    plt.plot([i,i],[0,h1[i]], color="blue")
    plt.plot([i,i],[h1[i],h2[i]], color="cyan")
    plt.plot([i,i],[h2[i],h3[i]], color="blue")
    plt.plot([i,i],[h3[i],h[i]], color="cyan")

plt.show()