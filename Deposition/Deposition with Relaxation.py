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
    a=np.var(h)**(0.5)
    return a

h=np.array([[0] for x in range(200)])
for x in range(10000):
    i=rand.randint(0,199)
    if i>0 and i<199:
        if h[i]<=min(h[i-1],h[i+1]) or (h[i]==h[i-1] and h[i]==h[i+1]):
            h[i]=h[i]+1
        elif h[i+1]>h[i-1]:
            h[i-1]=h[i-1]+1
        elif h[i-1]>h[i+1]:
            h[i+1]=h[i+1]+1
        elif h[i+1]==h[i-1]:
            m=rand.randint(0,1)
            if m==0:
                h[i+1]=h[i+1]+1
            else:
                h[i-1]=h[i-1]+1
    if i==0:
        if h[i]<=min(h[199],h[i+1]) or (h[i]==h[199] and h[i]==h[i+1]):
            h[i]=h[i]+1
        elif h[i+1]>h[199]:
            h[199]=h[199]+1
        elif h[199]>h[i+1]:
            h[i+1]=h[i+1]+1
        elif h[i+1]==h[199]:
            m=rand.randint(0,1)
            if m==0:
                h[i+1]=h[i+1]+1
            else:
                h[199]=h[199]+1 
    if i==199:
        if h[i]<=min(h[i-1],h[0]) or (h[i]==h[i-1] and h[i]==h[0]):
            h[i]=h[i]+1
        elif h[0]>h[i-1]:
            h[i-1]=h[i-1]+1
        elif h[i-1]>h[0]:
            h[0]=h[0]+1
        elif h[0]==h[i-1]:
            m=rand.randint(0,1)
            if m==0:
                h[0]=h[0]+1
            else:
                h[i-1]=h[i-1]+1    

h1=h.copy()
print(mean(h1.copy()))
print(dev(h1.copy()))

for x in range(10000):
    i=rand.randint(0,199)
    if i>0 and i<199:
        if h[i]<=min(h[i-1],h[i+1]) or (h[i]==h[i-1] and h[i]==h[i+1]):
            h[i]=h[i]+1
        elif h[i+1]>h[i-1]:
            h[i-1]=h[i-1]+1
        elif h[i-1]>h[i+1]:
            h[i+1]=h[i+1]+1
        elif h[i+1]==h[i-1]:
            m=rand.randint(0,1)
            if m==0:
                h[i+1]=h[i+1]+1
            else:
                h[i-1]=h[i-1]+1
    if i==0:
        if h[i]<min(h[199],h[i+1]):
            h[i]=h[i]+1
        elif h[i+1]>h[199]:
            h[199]=h[199]+1
        elif h[199]>h[i+1]:
            h[i+1]=h[i+1]+1
        elif h[i+1]==h[199]:
            m=rand.randint(0,1)
            if m==0:
                h[i+1]=h[i+1]+1
            else:
                h[199]=h[199]+1 
    if i==199:
        if h[i]<min(h[i-1],h[0]):
            h[i]=h[i]+1
        elif h[0]>h[i-1]:
            h[i-1]=h[i-1]+1
        elif h[i-1]>h[0]:
            h[0]=h[0]+1
        elif h[0]==h[i-1]:
            m=rand.randint(0,1)
            if m==0:
                h[0]=h[0]+1
            else:
                h[i-1]=h[i-1]+1  
h2=h.copy()
print(mean(h2.copy()))
print(dev(h2.copy()))

for x in range(10000):
    i=rand.randint(0,199)
    if i>0 and i<199:
        if h[i]<=min(h[i-1],h[i+1]) or (h[i]==h[i-1] and h[i]==h[i+1]):
            h[i]=h[i]+1
        elif h[i+1]>h[i-1]:
            h[i-1]=h[i-1]+1
        elif h[i-1]>h[i+1]:
            h[i+1]=h[i+1]+1
        elif h[i+1]==h[i-1]:
            m=rand.randint(0,1)
            if m==0:
                h[i+1]=h[i+1]+1
            else:
                h[i-1]=h[i-1]+1
    if i==0:
        if h[i]<min(h[199],h[i+1]):
            h[i]=h[i]+1
        elif h[i+1]>h[199]:
            h[199]=h[199]+1
        elif h[199]>h[i+1]:
            h[i+1]=h[i+1]+1
        elif h[i+1]==h[199]:
            m=rand.randint(0,1)
            if m==0:
                h[i+1]=h[i+1]+1
            else:
                h[199]=h[199]+1 
    if i==199:
        if h[i]<min(h[i-1],h[0]):
            h[i]=h[i]+1
        elif h[0]>h[i-1]:
            h[i-1]=h[i-1]+1
        elif h[i-1]>h[0]:
            h[0]=h[0]+1
        elif h[0]==h[i-1]:
            m=rand.randint(0,1)
            if m==0:
                h[0]=h[0]+1
            else:
                h[i-1]=h[i-1]+1  
h3=h.copy()
print(mean(h3.copy()))
print(dev(h3.copy()))

for x in range(10000):
    i=rand.randint(0,199)
    if i>0 and i<199:
        if h[i]<min(h[i-1],h[i+1]):
            h[i]=h[i]+1
        elif h[i+1]>h[i-1]:
            h[i-1]=h[i-1]+1
        elif h[i-1]>h[i+1]:
            h[i+1]=h[i+1]+1
        elif h[i+1]==h[i-1]:
            m=rand.randint(0,1)


            if m==0:
                h[i+1]=h[i+1]+1
            else:
                h[i-1]=h[i-1]+1
    if i==0:
        if h[i]<min(h[199],h[i+1]):
            h[i]=h[i]+1
        elif h[i+1]>h[199]:
            h[199]=h[199]+1
        elif h[199]>h[i+1]:
            h[i+1]=h[i+1]+1
        elif h[i+1]==h[199]:
            m=rand.randint(0,1)
            if m==0:
                h[i+1]=h[i+1]+1
            else:
                h[199]=h[199]+1 
    if i==199:
        if h[i]<min(h[i-1],h[0]):
            h[i]=h[i]+1
        elif h[0]>h[i-1]:
            h[i-1]=h[i-1]+1
        elif h[i-1]>h[0]:
            h[0]=h[0]+1
        elif h[0]==h[i-1]:
            m=rand.randint(0,1)
            if m==0:
                h[0]=h[0]+1
            else:
                h[i-1]=h[i-1]+1  
h4=h.copy()
print(mean(h4.copy()))
print(dev(h4.copy()))

for i in range(200):
    plt.plot([i,i],[0,h1[i]], color="blue")
    plt.plot([i,i],[h1[i],h2[i]], color="cyan")
    plt.plot([i,i],[h2[i],h3[i]], color="blue")
    plt.plot([i,i],[h3[i],h[i]], color="cyan")

plt.show()