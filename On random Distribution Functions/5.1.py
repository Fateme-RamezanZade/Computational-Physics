import random as rand
import numpy as np
import matplotlib.pyplot as plt
import math

def func(x):
    y=math.exp(-x**2)
    return y

n=10000
I=np.array([0. for i in range(100)])
for num in range(100):
    x_value=np.array([rand.uniform(0,2) for i in range(n)])
    y_value=np.array([func(x_value[i]) for i in range(n)])
    I[num]=np.mean(y_value)*2
print('I=%s'%(np.mean(I)))
print('sigma=%s'%(np.std(I)))