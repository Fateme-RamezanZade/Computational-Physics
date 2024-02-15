import numpy as np
import random as rand
import matplotlib.pyplot as plt
import math

l=1
num=1000
r_mean=np.array([0 for i in range(100)])

for time_step in range(100):
    time=time_step*20
    sum_x=0
    sum_y=0
    for i in range(num):
        x=0
        y=0
        for t in range(time):
            m=rand.randint(1,4)
            if m==1:
                x=x+l
            if m==2:
                x=x-l 
            if m==3:
                y=y+l
            if m==4:
                y=y-l 
        sum_x=sum_x+x**2
        sum_y=sum_y+y**2
    r_mean[time_step]=((sum_x+sum_y)/num)**(1/2)

for i in range(1,100):
    plt.plot([math.log(i*20)],[math.log(r_mean[i])],'bo',markersize=1)

x=np.array([math.log(20*i) for i in range(1,100)])
r_mean=np.array([math.log(r_mean[i]) for i in range(1,100)])

z = np.polyfit(x, r_mean, 1)
plt.plot([0,7.7],[z[1],7.7*z[0]+z[1]], color="cyan",label="y=%sx%s"%(round(z[0],3) ,round(z[1],3)))
plt.legend(loc="upper left")
plt.xlabel("t")
plt.ylabel("sqrt(<r^2>)")
plt.show()

