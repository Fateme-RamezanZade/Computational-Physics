import numpy as np
import random as rand
import matplotlib.pyplot as plt


l=1
num=10000
p=0.3
x_mean=np.array([0 for i in range(100)])
sigma=np.array([0 for i in range(100)])

for time_step in range(100):
    time=time_step*20
    sum=0
    sum2=0
    for i in range(num):
        x=0
        for t in range(time):
            m=rand.random()
            if m<p:
                x=x+l
            else:
                x=x-l  
        sum=sum+x
        sum2=sum2+x**2
    x_mean[time_step]=sum/num
    sigma[time_step]=(sum2/num-x_mean[time_step]**2)
'''
for i in range(100):
    plt.plot([i*20],[x_mean[i]],'ko',markersize=1)

x=np.array([20*i for i in range(100)])
z = np.polyfit(x, x_mean, 1)
plt.plot([0,2000],[z[1],2000*z[0]+z[1]], color="cyan",label="(p=0.3) y=%sx%s"%(round(z[0],3) ,round(z[1],3)))
'''
for i in range(100):
    plt.plot([i*20],[sigma[i]],'bo',markersize=1)
x=np.array([20*i for i in range(100)])
z = np.polyfit(x, sigma, 1)
plt.plot([0,2000],[z[1],2000*z[0]+z[1]], color="cyan",label="(p=0.3) y=%sx%s"%(round(z[0],3) ,round(z[1],3)))
    
print(x_mean , sigma)



p=0.5
x_mean=np.array([0 for i in range(100)])
sigma=np.array([0 for i in range(100)])

for time_step in range(100):
    time=time_step*20
    sum=0
    sum2=0
    for i in range(num):
        x=0
        for t in range(time):
            m=rand.random()
            if m<p:
                x=x+l
            else:
                x=x-l  
        sum=sum+x
        sum2=sum2+x**2
    x_mean[time_step]=sum/num
    sigma[time_step]=(sum2/num-x_mean[time_step]**2)
'''
for i in range(100):
    plt.plot([i*20],[x_mean[i]],'ko',markersize=1)

x=np.array([20*i for i in range(100)])
z = np.polyfit(x, x_mean, 1)
plt.plot([0,2000],[z[1],2000*z[0]+z[1]], color="green",label="(p=0.5) y=%sx%s"%(round(z[0],3) ,round(z[1],3)))
'''
for i in range(100):
    plt.plot([i*20],[sigma[i]],'ko',markersize=1)
x=np.array([20*i for i in range(100)])
z = np.polyfit(x, sigma, 1)
plt.plot([0,2000],[z[1],2000*z[0]+z[1]], color="green",label="(p=0.5) y=%sx%s"%(round(z[0],3) ,round(z[1],3)))
    
print(x_mean , sigma)



p=0.8
x_mean=np.array([0 for i in range(100)])
sigma=np.array([0 for i in range(100)])

for time_step in range(100):
    time=time_step*20
    sum=0
    sum2=0
    for i in range(num):
        x=0
        for t in range(time):
            m=rand.random()
            if m<p:
                x=x+l
            else:
                x=x-l  
        sum=sum+x
        sum2=sum2+x**2
    x_mean[time_step]=sum/num
    sigma[time_step]=(sum2/num-x_mean[time_step]**2)
'''
for i in range(100):
    plt.plot([i*20],[x_mean[i]],'ko',markersize=1)

x=np.array([20*i for i in range(100)])
z = np.polyfit(x, x_mean, 1)
plt.plot([0,2000],[z[1],2000*z[0]+z[1]], color="yellow",label="(p=0.8) y=%sx%s"%(round(z[0],3) ,round(z[1],3)))
'''
for i in range(100):
    plt.plot([i*20],[sigma[i]],'ro',markersize=1)
x=np.array([20*i for i in range(100)])
z = np.polyfit(x, sigma, 1)
plt.plot([0,2000],[z[1],2000*z[0]+z[1]], color="yellow",label="(p=0.8) y=%sx%s"%(round(z[0],3) ,round(z[1],3)))
    
print(x_mean , sigma)


plt.legend(loc="upper left")
plt.xlabel("t")
plt.ylabel("variance(t)")
plt.show()