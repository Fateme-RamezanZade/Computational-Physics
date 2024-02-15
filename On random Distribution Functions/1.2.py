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

std=np.array([0. for i in range(10)])
yerr=np.array([0. for i in range(10)])
for num in range(10):
    N=10*(num+1)
    std_sum=np.array([0. for i in range(100)])
    for turn in range(100):
        arr=np.array([rand.randint(0,9) for i in range(N)])
        n,bins=np.histogram(arr, bins=range(11))
        std_sum[turn]=np.std(n)
    yerr[num]=np.std(std_sum/N)
    std[num]=np.mean(std_sum)/(N)

n_arr_log=np.array([math.log(10*(i+1)) for i in range(len(std))])
std_log=np.array([math.log(std[i]) for i in range(len(std))])
yerr_log=np.array([yerr[i]**(-1/2)/100 for i in range(len(std))])

for x in range(len(std)):
    plt.plot(n_arr_log[x],std_log[x],'ro',markersize=3)
z = np.polyfit(n_arr_log, std_log, 1)
print(s_err(n_arr_log,std_log,z[0],z[1]))
plt.plot([1,5],[1*z[0]+z[1],5*z[0]+z[1]], color="cyan",label="y=%sx+%s"%(round(z[0],3) ,round(z[1],3)))

plt.errorbar(n_arr_log,std_log, yerr_log ,fmt ='o')
plt.legend(loc="upper left")
plt.xlabel("ln(1/sqrt(N))")
plt.ylabel("ln(sigma/N)")
plt.show()
