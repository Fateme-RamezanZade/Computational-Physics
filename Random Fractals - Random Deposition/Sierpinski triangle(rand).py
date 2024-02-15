import matplotlib.pyplot as plt
import numpy as np
import random as rand

def Homogeneity_func(points):
    points_n=points
    points_n[0]=1/2*points[0]
    points_n[1]=1/2*points[1]
    return points_n
#multipules size by 1/2

def Shift_func(points, delta):
    points_n=points
    points_n[0]=points[0]+delta[0]
    points_n[1]=points[1]+delta[1]
    return points_n
#shifts shape with (delta[])


for x in range(20000):
    x=rand.randint(0,100)
    y=rand.randint(0,100)
    points=np.array([x,y])
    #points=[0,1]
    for i in range(20):
        func=rand.randint(1,3)
        #func=1
        if func==1:
            points=Homogeneity_func(points.copy())
        if func==2:
            delta=np.array([150,0])
            points=Shift_func(Homogeneity_func(points.copy()), delta)
        if func==3:
            delta=np.array([150/2,129.9])
            points=Shift_func(Homogeneity_func(points.copy()), delta)
    plt.plot(points[0],points[1],'ro',markersize=1) 
plt.show()





'''


points =np.array([ [0,0],[1,0],[0.5,0.86]]) 
num=7

for x in range(num):

    points_c=points.copy()
    points1=Homogeneity_func(points_c)
    points1x=np.array([points1[i][0] for i in range(len(points1))])
    points1y=np.array([points1[i][1] for i in range(len(points1))])
    delta1=[[np.amax(points1x)-points1[0][0],0]]
    delta2=[[(np.amax(points1x)-points1[0][0])/2,np.amax(points1y)-points1[0][1]]]
    points1_c=points1.copy()
    points1_cc=points1.copy()
    points2=Shift_func(points1_c, delta1)
    points2_c=points2.copy()
    points3=Shift_func(points1_cc, delta2)
    points3_c=points3.copy()
    newpoints=np.concatenate((points1,points2,points3),axis=0)
    points=newpoints

plottri(points)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()
'''