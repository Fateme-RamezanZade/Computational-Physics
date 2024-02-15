import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math

def s_err(x,y,slope,y0):
    mean=np.mean(x)
    s1=0
    s2=0
    for i in range(len(x)):
        s1+=(y[i]-(slope*x[i]+y0))**2
        s2+=(x[i]-mean)**2
    return (s1/s2/(len(x)-2))**(1/2)

std=np.array([0. for i in range(100)])
N_arr=np.array([0. for i in range(100)])

for turn in range(100):
    data=np.array([0])
    N=100*(turn+1)
    arr=np.array([rand.randint(0,9) for i in range(N)])
    n=0
    for i in range(len(arr)-1):
        if arr[i+1]==4:
            data=np.append(data,0)
            data[n]=arr[i]
            n+=1
    data=np.delete(data, len(data)-1)
    N_arr[turn]=len(data)
    n,bins=np.histogram(data, bins=range(11))
    std[turn]=np.std(n)/len(data)

n_arr_log=np.array([math.log(N_arr[i]) for i in range(len(N_arr))])
std_log=np.array([math.log(std[i]) for i in range(len(std))])

for x in range(len(N_arr)):
    plt.plot(n_arr_log[x],std_log[x],'ro',markersize=3)

z = np.polyfit(n_arr_log, std_log, 1)
print(s_err(n_arr_log,std_log,z[0],z[1]))
plt.plot([2,7],[2*z[0]+z[1],7*z[0]+z[1]], color="cyan",label="y=%sx+%s"%(round(z[0],3) ,round(z[1],3)))
plt.legend(loc="upper left")
plt.xlabel("ln(1/sqrt(N))")
plt.ylabel("ln(sigma/N)")
plt.show()