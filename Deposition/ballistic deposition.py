import matplotlib.pyplot as plt
import numpy as np
import random as rand

def dev(h):
    a=np.var(h)**(0.5)
    return a

def height(h,t):
    height=0
    for t in reversed(range(t)):
        if h[t]==1:
            height=t
            break
    return height

def color(i):
    if (i>=0 and i<5000) or (i>=10000 and i<15000):
        return 'blue'
    if (i>=5000 and i<10000) or (i>=15000):
        return 'cyan'

t=20000
l=200

h=np.array([[0,0] for x in range(l)])
hheight=np.array([[0] for x in range(l)])
for x in range(t+1):
    i=rand.randint(0,l-1)
    if i>0 and i<l-1:

        if height(h[i],x)>max(height(h[i-1],x),height(h[i+1],x)) or (height(h[i],x)==height(h[i-1],x) and height(h[i],x)==height(h[i+1],x)):
            h[i][height(h[i],x)+1]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)>height(h[i-1],x):
            h[i][height(h[i+1],x)]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)<height(h[i-1],x):
            h[i][height(h[i-1],x)]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
            
        elif height(h[i+1],x)==height(h[i-1],x):
            m=rand.randint(0,1)
            if m==0:
                h[i][height(h[i-1],x)]=1
                plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
            else:
                h[i][height(h[i+1],x)]=1
                plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))   

    if i==0:
        if height(h[i],x)>max(height(h[l-1],x),height(h[i+1],x)) or (height(h[i],x)==height(h[l-1],x) and height(h[i],x)==height(h[i+1],x)):
            h[i][height(h[i],x)+1]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)>height(h[l-1],x):
            h[i][height(h[l-1],x)]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)<height(h[l-1],x):
            h[i][height(h[l-1],x)]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)==height(h[l-1],x):
            m=rand.randint(0,1)
            if m==0:
                h[i][height(h[l-1],x)]=1
                plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
            else:
                h[i][height(h[i+1],x)]=1
                plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
 
    if i==l-1:
        if height(h[i],x)>max(height(h[i-1],x),height(h[0],x)) or (height(h[i],x)==height(h[i-1],x) and height(h[i],x)==height(h[0],x)):
            h[i][height(h[i],x)+1]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
        elif height(h[0],x)>height(h[i-1],x):
            h[i][height(h[0],x)]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
        elif height(h[0],x)<height(h[i-1],x):
            h[i][height(h[i-1],x)]=1
            plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
        elif height(h[0],x)==height(h[i-1],x):
            m=rand.randint(0,1)
            if m==0:
                h[i][height(h[i-1],x)]=1
                plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
            else:
                h[i][height(h[0],x)]=1
                plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))
    h=np.append(h,[[0] for i in range(l)],axis=1) 
    if x%(t/4)==0:
        for m  in range(l):
            hheight[m]=height(h[m],x)
        print(np.mean(hheight))
        print(dev(hheight))

plt.gca().set_aspect('equal', adjustable='box')
 

plt.show()