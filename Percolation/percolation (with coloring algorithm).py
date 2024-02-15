import numpy as np
import matplotlib.pyplot as plt
import random as rand


l=10
p=0.5
color=1
c1=0
c2=0
arr=np.array([[[0] for i in range (l)] for j in range (l)])
for i in range(l):
    arr[0][i]=1
color=color+1

for i in range(1,l):
    for j in range(l):
        m=rand.random()
        if m<p:
            if arr[i][j-1]!=0 and arr[i-1][j]!=0:
                arr[i][j]=min(arr[i][j-1],arr[i-1][j])
                c1=arr[i][j-1]
                c2=arr[i-1][j]
                for m in range(i+1):
                    for n in range(l):
                        if arr[m][n]==c1 or arr[m][n]==c2:
                            arr[m][n]=arr[i][j]
            elif arr[i][j-1]!=0 or arr[i-1][j]!=0:
                if arr[i][j-1]!=0:
                    arr[i][j]=arr[i][j-1]
                else:
                    arr[i][j]=arr[i-1][j]
            else:
                arr[i][j]=color
                color=color+1
val=0
for i in range(l):
    if val==1:
        break
    else:
        for j in range(l):
            if arr[l-1][j]==0:
                val=1
                break
print(val)
code=np.array([[[0] for i in range (l)] for j in range (l)]) 
for i in range(l):
    for j in range(l):
        code[i][j]=arr[j][i]

plt.imshow(code,cmap='cubehelix')
plt.show()