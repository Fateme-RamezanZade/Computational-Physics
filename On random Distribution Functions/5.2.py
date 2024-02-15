import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math

def func(x):
    y=math.exp(-x**2)
    return y

def dist(x):
    y=-1*math.log(1-x/2)
    return y

def g(x):
     y=math.exp(-x)
     return y

n=10000
I=np.array([0. for i in range(100)])
for num in range(100):
    x_value=np.array([0. for i in range(n)])
    for i in range(n):
        number=rand.uniform(0,2)
        while(dist(number)>2):
            number=rand.uniform(0,2)
        x_value[i]=dist(number)  
    y_value=np.array([func(x_value[i])/g(x_value[i]) for i in range(n)])
    I[num]=(np.mean(y_value)*0.8646647167633873)
print('I=%s'%(np.mean(I)))
print('sigma=%s'%(np.std(I)))