import numpy as np
import random as rand
import matplotlib.pyplot as plt

l=1
num=1000

p=0.3
q=1-p
life_x=np.array([0 for i in range(21)])
for x_0 in range(21):
    prob=np.array([[0. for i in range(21)],[0. for i in range(21)]])
    prob[0][x_0]=1
    j=1
    lifetime=0
    while True:
        prob=np.append(prob,[[0. for m in range(21)]],axis=0)
        for i in range(21):
            if i>1 and i<19:
                prob[j][i]=prob[j-1][i-1]*p+prob[j-1][i+1]*q
            elif i==1:
                prob[j][i]=prob[j-1][i+1]*q
            elif i==19:
                prob[j][i]=prob[j-1][i-1]*p
            elif i==20:
                prob[j][i]=prob[j-1][i]+prob[j-1][i-1]*p
            elif i==0:
                prob[j][i]=prob[j-1][i]+prob[j-1][i+1]*q
        lifetime=lifetime+(prob[j][0]+prob[j][20]-prob[j-1][0]-prob[j-1][20])*j
        if prob[j][0]+prob[j][20]>0.9999:
            life_x[x_0]=lifetime
            break
        j=j+1
for i in range(21):
    if i==0:
        plt.plot([i],[life_x[i]],'co', markersize=2,label="p=0.3")
    else:
        plt.plot([i],[life_x[i]],'co', markersize=2)


p=0.5
q=1-p
life_x=np.array([0 for i in range(21)])
for x_0 in range(21):
    prob=np.array([[0. for i in range(21)],[0. for i in range(21)]])
    prob[0][x_0]=1
    j=1
    lifetime=0
    while True:
        prob=np.append(prob,[[0. for m in range(21)]],axis=0)
        for i in range(21):
            if i>1 and i<19:
                prob[j][i]=prob[j-1][i-1]*p+prob[j-1][i+1]*q
            elif i==1:
                prob[j][i]=prob[j-1][i+1]*q
            elif i==19:
                prob[j][i]=prob[j-1][i-1]*p
            elif i==20:
                prob[j][i]=prob[j-1][i]+prob[j-1][i-1]*p
            elif i==0:
                prob[j][i]=prob[j-1][i]+prob[j-1][i+1]*q
        lifetime=lifetime+(prob[j][0]+prob[j][20]-prob[j-1][0]-prob[j-1][20])*j
        if prob[j][0]+prob[j][20]>0.9999:
            life_x[x_0]=lifetime
            break
        j=j+1
for i in range(21):
    if i==0:
        plt.plot([i],[life_x[i]],'go', markersize=2,label="p=0.5")
    else:
        plt.plot([i],[life_x[i]],'go', markersize=2)

p=0.8
q=1-p
life_x=np.array([0 for i in range(21)])
for x_0 in range(21):
    prob=np.array([[0. for i in range(21)],[0. for i in range(21)]])
    prob[0][x_0]=1
    j=1
    lifetime=0
    while True:
        prob=np.append(prob,[[0. for m in range(21)]],axis=0)
        for i in range(21):
            if i>1 and i<19:
                prob[j][i]=prob[j-1][i-1]*p+prob[j-1][i+1]*q
            elif i==1:
                prob[j][i]=prob[j-1][i+1]*q
            elif i==19:
                prob[j][i]=prob[j-1][i-1]*p
            elif i==20:
                prob[j][i]=prob[j-1][i]+prob[j-1][i-1]*p
            elif i==0:
                prob[j][i]=prob[j-1][i]+prob[j-1][i+1]*q
        lifetime=lifetime+(prob[j][0]+prob[j][20]-prob[j-1][0]-prob[j-1][20])*j
        if prob[j][0]+prob[j][20]>0.9999:
            life_x[x_0]=lifetime
            break
        j=j+1
for i in range(21):
    if i==0:
        plt.plot([i],[life_x[i]],'yo', markersize=2,label="p=0.8")
    else:
        plt.plot([i],[life_x[i]],'yo', markersize=2)

plt.legend(loc="upper left")
plt.xlabel("x_0")
plt.ylabel("life time")
plt.show()