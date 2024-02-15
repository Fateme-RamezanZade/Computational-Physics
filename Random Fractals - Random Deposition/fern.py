import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math

def Homogeneity_func(points,m_x,m_y):
    points_n=points
    points_n[0]=m_x*points[0]
    points_n[1]=m_y*points[1]
    return points_n
#multipules size by m_x,m_y

def Shift_func(points, delta):
    points_n=points
    points_n[0]=points[0]+delta[0]
    points_n[1]=points[1]+delta[1]
    
    return points_n
#shifts shape with (delta[])

def Reflection_func(points):
    points_n=points
    points_n[0]=-points[0]
    return points_n
#reflects point about y axis

def Rotation_func(points,angle):
    points_n=np.array([0.,0.])
    points_n[0]=points[0]*math.cos(angle)-points[1]*math.sin(angle)
    points_n[1]=points[1]*math.cos(angle)+points[0]*math.sin(angle)
    return points_n
#rotates poinr about origin with (angle) radians


for x in range(50000):
    x=rand.randint(0,100)
    y=rand.randint(0,100)
    points=np.array([float(x),float(y)])
    for i in range(20):
        func=rand.randint(1,10)
        if func>3:
            delta=np.array([4.5,17.5])
            points=Homogeneity_func(points.copy(),0.828,0.853)
            points=Rotation_func(points.copy(),-0.052)
            points=Shift_func(points.copy(),delta)
            
        
        if func==3:
            delta=np.array([22,12])
            points=Homogeneity_func(points.copy(),0.295,0.339)
            points=Rotation_func(points.copy(),0.855)
            points=Shift_func(points.copy(),delta)
            
        
        if func==2:
            delta=np.array([32.,-2.])
            points=Homogeneity_func(points.copy(),0.288,0.366)
            points=Reflection_func(points.copy())
            points=Rotation_func(points.copy(),-0.872)
            points=Shift_func(points.copy(),delta)
            
        
        if func==1: 
            p1=points.copy()
            delta=np.array([27.,0.])
            p1=Homogeneity_func(p1.copy(),0.000001,0.16)
            p1=Shift_func(p1.copy(),delta)
            points=p1
        


    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.plot(points[0],points[1],'bo',markersize=0.5) 
plt.show()

