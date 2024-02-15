import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math

h=np.array([[0] for x in range(200)])
theta=math.pi/3
l=200
height=100
for x in range(5000):
    i=rand.randint(0,l)
    for j in range(l-i):
        if h[j+i]>=i*math.tan(theta)-j*math.tan(theta):
            h[j+i]=h[j+i]+1
            break

for i in range(200):
    plt.plot([i,i],[0,h[i]], color="blue")

plt.show()