import numpy as np
import random as rand
import matplotlib.pyplot as plt


def color(n,number):
    if n<number/4:
        return 'red'
    elif n<number/2:
        return 'blue'
    elif n<number*3/4:
        return 'green'
    else:
        return 'yellow'
    
def h(arr):
    for i in reversed(range(len(arr))):
        if arr[i]==1:
            return i
            

number=5000
length=200
l=1
arr=np.array([[0 for i in range(20)] for j in range(length)])
height=0
for i in range(length):
     arr[i][0]=1
     plt.plot([i],[0],'rs',markersize=1)


for n in range(number):
    x=rand.randint(0,length-1)
    y0=height+2
    y=height+2
    while x>0 and x<length-1 and y<y0+20:
        if y<len(arr[x])-1:
            if arr[x+1][y]==1 or arr[x-1][y]==1 or arr[x][y+1] or arr[x][y-1]:
                 arr[x][y]=1
                 plt.plot([x],[y],'s', markersize=1, color=color(n,number))
                 arr=np.append(arr,[[0] for i in range(length)],axis=1)
                 if y>height:
                     height=y
                 break
        m=rand.randint(1,4)
        if m==1:
            x=x+l
        if m==2:
            x=x-l 
        if m==3:
            y=y+l
        if m==4:
            y=y-l

plt.gca().set_aspect('equal', adjustable='box')
plt.show() 