import numpy as np
import math
import matplotlib.pyplot as plt
import random as rand

def p(x):
    sigma=1
    return (2*math.pi*sigma)**(-0.5)*math.exp(-x**2/(2*sigma**2))

def c(j,arr_x):
    sum1=0
    for i in range(len(arr_x)-j):
        sum1+=arr_x[i]*arr_x[(i+j)%len(arr_x)]
    mean1=sum1/(len(arr_x)-j)
    mean2=np.mean(x_arr)**2
    std=np.std(arr_x)
    return (mean1-mean2)/(std**2)
    
N=1000
repeat=100
j_length=10

delta=1.
rate=0
cor_arr=np.array([0. for a in range(100)])
for num in range(repeat):
    x=0
    x_arr=np.array([x])
    for n in range(N):
        j=rand.random()
        if j<0.5:
            i=1.
        else:
            i=-1.
        i=np.random.uniform(-1,1)
        y=x+i*delta
        if p(x)>0:
            r=rand.random()
            if r<(p(y)/p(x)):
                x=y
                x_arr=np.append(x_arr,[x])        
    rate+=(len(x_arr)-1)/N
    #print(rate)
    c_arr=np.array([c(a,x_arr) for a in range(j_length)])
    for b in range(j_length):
        cor_arr[b]+=c_arr[b]
cor_mean=np.array([cor_arr[i]/repeat for i in range(j_length)])
rate=rate/repeat

"""for i in range(len(cor_mean)):
    if i==0:
        plt.plot(i,(cor_mean[i]),'ro',markersize=2,label='a.rate=%s'%(round(rate,2)))
    if i>0:
        plt.plot(i,(cor_mean[i]),'ro',markersize=2)"""

cor_mean_log=np.log(cor_mean)
#print(cor_mean_log)
j_arr=np.array([i for i in range(j_length)])
#plt.plot(j_arr,cor_mean_log,'ro')
z = np.polyfit(j_arr, cor_mean_log, 1)
"""plt.plot([0,10],[z[1],10*z[0]+z[1]], color="cyan",label="a.r.=%s y=%sx%s"%(round(rate,2), round(z[0],3) ,round(z[1],3)))
plt.legend(loc='upper left')"""
print(-1/z[0])