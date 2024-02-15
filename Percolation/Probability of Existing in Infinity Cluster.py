import numpy as np
import matplotlib.pyplot as plt
import random as rand


length=10
q_inf=np.array([[0.] for i in range(21)])
for x in range(21):
    p=0.05*x
    q_infinity=0.
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
                            q_infinity=q_infinity+max(s)/(sum(s))
                            break
    q_inf[x]=q_infinity/100.
print(q_inf)
for x in range(len(q_inf)):
    if x==0:
        plt.plot(x/20,q_inf[x],'ro',label="(L=%s)"%(length))
    else:
        plt.plot(x/20,q_inf[x],'ro')  

length=100
q_inf=np.array([[0.] for i in range(21)])
for x in range(21):
    p=0.05*x
    q_infinity=0.
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
                            q_infinity=q_infinity+max(s)/(sum(s))
                            break
    q_inf[x]=q_infinity/100.
print(q_inf)
for x in range(len(q_inf)):
    if x==0:
        plt.plot(x/20,q_inf[x],'bo',label="(L=%s)"%(length))
    else:
        plt.plot(x/20,q_inf[x],'bo')

length=200
q_inf=np.array([[0.] for i in range(21)])
for x in range(21):
    p=0.05*x
    q_infinity=0.
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
                            q_infinity=q_infinity+max(s)/(sum(s))
                            break
    q_inf[x]=q_infinity/100.
print("for l=%s"%(length))
print(q_inf)
for x in range(len(q_inf)):
    if x==0:
        plt.plot(x/20,q_inf[x],'go',label="(L=%s)"%(length))
    else:
        plt.plot(x/20,q_inf[x],'go')

plt.xlabel("p")
plt.ylabel("Q_infty")
plt.legend(loc="upper left")
plt.show()



