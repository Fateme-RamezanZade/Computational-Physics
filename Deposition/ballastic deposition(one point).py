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
def width(h):
    l1=0
    l2=0
    for i in range(len(h)):
        if h[i]==1:
            l1=i
            break
    for i in reversed(range(len(h))):
        if h[i]==1:
            l2=i
            break
    return l2-l1


    


h=np.array([[0,0] for x in range(200)])
length=np.array([[0] for x in range(50)])
cor=np.array([[0] for x in range(50)])
w=np.array([0])
h[100][0]=1
#plt.plot(100,0, marker="s", markersize=1,color=color(0))
for x in range(1,5000):
    i=rand.randint(0,199)
    if i>0 and i<199:

        if height(h[i],x)>max(height(h[i-1],x),height(h[i+1],x)):
            h[i][height(h[i],x)+1]=1
            #plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i],x)==height(h[i-1],x) and height(h[i],x)==height(h[i+1],x):
            if h[i][height(h[i],x)]!=0:
               h[i][height(h[i],x)+1]=1
               #plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)>height(h[i-1],x):
            h[i][height(h[i+1],x)]=1
            #plt.plot(i,height(h[i+1],x), marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)<height(h[i-1],x):
            h[i][height(h[i-1],x)]=1
            #plt.plot(i,height(h[i-1],x), marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)==height(h[i-1],x):
            if h[i][height(h[i],x)]!=0:
                m=rand.randint(0,1)
                if m==0:
                    h[i][height(h[i-1],x)]=1
                    #plt.plot(i,height(h[i-1],x), marker="s", markersize=1,color=color(x))
                else:
                    h[i][height(h[i+1],x)]=1  
                    #plt.plot(i,height(h[i+1],x), marker="s", markersize=1,color=color(x)) 

    if i==0:
        if height(h[i],x)>max(height(h[199],x),height(h[i+1],x)):
            h[i][height(h[i],x)+1]=1
            #plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i],x)==height(h[199],x) and height(h[i],x)==height(h[i+1],x):
            if h[i][height(h[i],x)]!=0:
               h[i][height(h[i],x)+1]=1
               #plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)>height(h[199],x):
            h[i][height(h[i+1],x)]=1
            #plt.plot(i,height(h[i+1],x), marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)<height(h[199],x):
            h[i][height(h[199],x)]=1
            #plt.plot(i,height(h[199],x), marker="s", markersize=1,color=color(x))

        elif height(h[i+1],x)==height(h[199],x):
            if h[i][height(h[i],x)]!=0:
                m=rand.randint(0,1)
                if m==0:
                    h[i][height(h[199],x)]=1
                    #plt.plot(i,height(h[199],x), marker="s", markersize=1,color=color(x))
                else:
                    h[i][height(h[i+1],x)]=1
                    #plt.plot(i,height(h[i+1],x), marker="s", markersize=1,color=color(x))
 
    if i==199:
        if height(h[i],x)>max(height(h[i-1],x),height(h[0],x)):
            h[i][height(h[i],x)+1]=1
            #plt.plot(i,height(h[i],x)+1, marker="s", markersize=1,color=color(x))

        elif height(h[i],x)==height(h[i-1],x) and height(h[i],x)==height(h[0],x):
            if h[i][height(h[i],x)]!=0:
               h[i][height(h[i],x)+1]=1
               #plt.plot(i,height(h[i],x), marker="s", markersize=1,color=color(x))

        elif height(h[0],x)>height(h[i-1],x):
            h[i][height(h[0],x)]=1
            #plt.plot(i,height(h[0],x), marker="s", markersize=1,color=color(x))

        elif height(h[0],x)<height(h[i-1],x):
            h[i][height(h[i-1],x)]=1
            #plt.plot(i,height(h[i-1],x), marker="s", markersize=1,color=color(x))

        elif height(h[0],x)==height(h[i-1],x):
            if h[i][height(h[i],x)]!=0:
                m=rand.randint(0,1)
                if m==0:
                    h[i][height(h[i-1],x)]=1
                    #plt.plot(i,height(h[i-1],x), marker="s", markersize=1,color=color(x))
                else:
                    h[i][height(h[0],x)]=1
                    #plt.plot(i,height(h[0],x), marker="s", markersize=1,color=color(x))

    h=np.append(h,[[0] for i in range(200)],axis=1) 
    
    w=np.append(w,[0])
    if x%100==0:
        l1=0
        l2=0
        for m in range(x):
            for n in range(200):
                if h[n][m]==1:
                    l1=n
                    break
            for n in reversed(range(200)):
                if h[n][m]==1:
                    l2=n
                    break
            w[m]=l2-l1
        cor[int(x/100)]=np.max(w)


x=np.zeros(int(50))
y=np.zeros(int(50))
for n in range(1,50):
    if cor[n]!=0:
        x[n]=math.log(n*100)
        y[n]=math.log(cor[n])
        plt.plot(x[n],y[n],'bo',markersize=0.5)
x=x[1:len(x)]
y=y[1:len(y)]
z1 = np.polyfit(x, y, 1)
plt.plot([5,8],[5*z1[0]+z1[1],8*z1[0]+z1[1]], color="cyan",label="y1=%sx%s"%(round(z1[0],3) ,round(z1[1],3)))
plt.legend(loc="upper left")
plt.xlabel("t")
plt.ylabel("w(t)")
'''
for i in range(200):
    for x in range(100000):
        if h[i][x]==1:
            plt.plot(i,x, marker="s", markersize=1,color='blue')
'''
#plt.gca().set_aspect('equal', adjustable='box')
plt.show()