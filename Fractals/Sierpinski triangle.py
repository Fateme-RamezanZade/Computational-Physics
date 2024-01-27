import matplotlib.pyplot as plt
import numpy as np

def Homogeneity_func(points):
    points_n=points
    for x in range(len(points_n)):
        if x<len(points_n):
            points_n[x][0]=1/2*(points[x][0]-points[0][0])+points[0][0]
            points_n[x][1]=1/2*(points[x][1]-points[0][1])+points[0][1]
    return points_n
#multipules size by 1/2

def Shift_func(points, delta):
    points_n=points
    for x in range(len(points)):
        if x<len(points):
            points_n[x][0]=points[x][0]+delta[0][0]
            points_n[x][1]=points[x][1]+delta[0][1]
    return points_n
#shifts shape with (delta[][])

def plottri(points):
    points_set_lst = np.array_split(points, len(points)/3)
    for i in range(len(points_set_lst)):
        points_set=np.asarray(points_set_lst[i])
        arr=np.array([[points_set[0][0],points_set[0][1]]])
        points_set_n=np.append(points_set, arr, axis=0)
        for x in range(len(points_set_n)):
            if x+1<len(points_set_n):
                plt.plot([points_set_n[x][0],points_set_n[x+1][0]],[points_set_n[x][1],points_set_n[x+1][1]],color="red")
#plots a triangle with each 3 points in the array respectively


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