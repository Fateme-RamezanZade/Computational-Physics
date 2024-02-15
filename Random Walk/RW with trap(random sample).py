import numpy as np
import random as rand
import matplotlib.pyplot as plt


l=1
num=10000

p=0.3
life_x=np.array([0 for i in range(21)])
for step in range(21):
    sum=0
    for i in range(num):
        x=step
        life=0
        while x<20 and x>0:
            m=rand.random()
            if m<p:
                x=x+l
            else:
                x=x-l
            life=life+1 
        sum=sum+life
    life_mean=sum/num
    life_x[step]=life_mean
for i in range(21):
    if i==0:
        plt.plot([i],[life_x[i]],'co', markersize=2,label="p=0.3")
    else:
        plt.plot([i],[life_x[i]],'co', markersize=2)

p=0.5
life_x=np.array([0 for i in range(21)])
for step in range(21):
    sum=0
    for i in range(num):
        x=step
        life=0
        while x<20 and x>0:
            m=rand.random()
            if m<p:
                x=x+l
            else:
                x=x-l
            life=life+1 
        sum=sum+life
    life_mean=sum/num
    life_x[step]=life_mean
for i in range(21):
    if i==0:
        plt.plot([i],[life_x[i]],'go', markersize=2,label="p=0.5")
    else:
        plt.plot([i],[life_x[i]],'go', markersize=2)


p=0.8
life_x=np.array([0 for i in range(21)])
for step in range(21):
    sum=0
    for i in range(num):
        x=step
        life=0
        while x<20 and x>0:
            m=rand.random()
            if m<p:
                x=x+l
            else:
                x=x-l
            life=life+1 
        sum=sum+life
    life_mean=sum/num
    life_x[step]=life_mean
for i in range(21):
    if i==0:
        plt.plot([i],[life_x[i]],'yo', markersize=2,label="p=0.8")
    else:
        plt.plot([i],[life_x[i]],'yo', markersize=2)


plt.legend(loc="upper left")
plt.xlabel("x_0")
plt.ylabel("life time")
plt.show()