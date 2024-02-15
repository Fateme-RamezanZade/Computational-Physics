import numpy as np
import matplotlib.pyplot as plt
import random as rand

def com(arr,l):
    com_x=np.array([[0.] for i in range(len(l))])
    com_y=np.array([[0.] for i in range(len(l))])
    for t in range(len(l)):
        num=0
        sum_x=0
        sum_y=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j]==l[t]:
                    sum_x=sum_x+i
                    sum_y=sum_y+j
                    num=num+1
        if num!=0:
            com_x[t]=sum_x/num
            com_y[t]=sum_y/num
    return com_x,com_y

def gy_rad(arr,l):
    rad=np.array([[0.] for i in range(len(l))])
    for t in range(len(l)):
        sum_r=0
        num=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j]==l[t]:
                    delta_x=com(arr,l)[0][t]-i
                    delta_y=com(arr,l)[1][t]-j
                    r=(delta_x**2+delta_y**2)
                    sum_r=sum_r+r
                    num=num+1
        if num!=0:
            rad[t]=(sum_r/num)**(1/2)
    rad=np.delete(rad,0)
    return rad



length=10
cor_len=np.array([[0.] for i in range(21)])
for x in range(21):
    p=0.05*x
    cor_length=0.
    for t in range(100):
        l=np.array([0,1])
        s=np.array([0,1])
        color=1
        arr=np.array([[[0] for i in range (length)] for j in range (length)])

        for i in range(length):
            for j in range(length):
                m=rand.random()
                if m<p:
                    if arr[i-1][j]==0:
                        if arr[i][j-1]==0:
                            arr[i][j]=l[color]
                            s[l[color]]=s[l[color]]+1
                            color=color+1
                            l=np.append(l,color)
                            s=np.append(s,0)
                        else:
                            arr[i][j]=arr[i][j-1]
                            s[arr[i][j-1]]=s[arr[i][j-1]]+1
                    else:
                        arr[i][j]=arr[i-1][j]
                        s[arr[i-1][j]]=s[arr[i-1][j]]+1
                        if arr[i][j-1]!=0:
                            if arr[i][j-1]!=arr[i-1][j]:
                                s[arr[i-1][j]]=s[arr[i-1][j]]+s[arr[i][j-1]]
                                s[arr[i][j-1]]=0
                                arr[i][j-1]=arr[i-1][j]
        val=0
        for i in range(length):
            if val==1:
                break
            else:
                for j in range(length):
                    if arr[0][i]==arr[length-1][j]:
                        if arr[0][i]!=0:
                            val=1
                            inf_color=arr[0][i]
                            break
        gy_radius=gy_rad(arr,l)
        if val==1:
            infty=np.max(gy_radius)
            inf=np.where(gy_radius==infty)
            gy_radius=np.delete(gy_radius, inf[0])
            
        cor_length=np.mean(gy_radius)+cor_length
    cor_len[x]=cor_length/100
print("for l=%s"%(length))
print(cor_len)

for x in range(len(cor_len)):
    if x==0:
        plt.plot(x/20,cor_len[x],'ro',markersize=3,label="(L=%s)"%(length))
    else:
        plt.plot(x/20,cor_len[x],'ro',markersize=3)


plt.xlabel("p")
plt.ylabel("cor. length")
plt.legend(loc="upper left")
plt.show()

