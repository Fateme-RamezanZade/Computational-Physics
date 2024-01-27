import array as arr
import math
import matplotlib.pyplot as plt

def Homogeneity_func(points, points_y):
    points_n=arr.array('d',(0 for x in range(len(points))))
    points_n[0]=points[0]
    for x in range(len(points)):
        if x<len(points):
            points_n[x]=1/3*(points[x]-points[0])+points[0]
    points_ny=arr.array('d',(0 for x in range(len(points_y))))
    points_ny[0]=points_y[0]
    for x in range(len(points_y)):
        if x<len(points_y):
            points_ny[x]=1/3*(points_y[x]-points_y[0])+points_y[0]
    return points_n, points_ny
#multipules size by 1/3

def Reflection_func(points, points_y):
    points_n=arr.array('d',(0 for x in range(len(points))))
    points_nn=arr.array('d',(0 for x in range(len(points))))
    points_ny=arr.array('d',(0 for x in range(len(points))))
    for x in range(len(points)):
        if( x<len(points)):
            points_n[x]=2*(points[len(points)-1]-points[x])+points[x]
    points_n[len(points)-1]=points[len(points)-1]
    for x in range(len(points_n)):
        points_nn[x]=points_n[len(points_n)-1-x]
    for x in range(len(points_y)):
        points_ny[x]=points_y[len(points_y)-1-x]
    return points_nn, points_ny
#reflects shape in x axis about last point

def Rotation_func(points_x,points_y,angle):
    points_nx=arr.array('d',(0 for x in range(len(points_x))))
    points_nx[0]=points_x[0]
    points_ny=arr.array('d',(0 for x in range(len(points_y))))
    points_ny[0]=points_y[0]
    for x in range(len(points_x)):
        if x!=0:
            points_nx[x]=(points_x[x]-points_x[0])*math.cos(angle)-(points_y[x]-points_y[0])*math.sin(angle)+points_x[0]
            points_ny[x]=(points_x[x]-points_x[0])*math.sin(angle)+(points_y[x]-points_y[0])*math.cos(angle)+points_y[0]
    return  points_nx,  points_ny
#rotates shape about first point (angle) radians
    
def Shift_func(points, points_y,delta):
    points_n=arr.array('d',(0 for x in range(len(points))))
    points_n[0]=points[0]+delta
    for x in range(len(points)):
        if x<len(points):
            points_n[x]=points[x]+delta
    return points_n, points_y
#shifts shape in x axis with (delta)

def Merge_func(points1,points2,points1_y,points2_y):
    points_nx=arr.array('d',(0 for x in range(len(points1)+len(points2)-1)))
    points_nx[0]=points1[0]
    for x in range(len(points_nx)):
        if x<len(points1):
            points_nx[x]=points1[x]
        if x>=len(points1):
            points_nx[x]=points2[x+1-len(points1)]
    points_ny=arr.array('d',(0 for x in range(len(points1_y)+len(points2_y)-1)))
    points_ny[0]=points1_y[0]
    for x in range(len(points_ny)):
        if x<len(points1_y):
            points_ny[x]=points1_y[x]
        if x>=len(points1_y):
            points_ny[x]=points2_y[x+1-len(points1_y)]
    return points_nx, points_ny
#merges two sets of points into one

def Plot_func(points_x,points_y):
    for x in range(len(points_x)):
        if x+1<len(points_x):
            plt.plot([points_x[x],points_x[x+1]],[points_y[x],points_y[x+1]], color="blue")
#given two arrays of coordinate of a set of points, plots respective lines with each two.
            

points_x=arr.array('d',[0,1])
points_y=arr.array('d',[0,0])
angle=math.pi/3
num=4
for x in range(num):
    points_x1,points_y1=Homogeneity_func(points_x, points_y)
    points_x2,points_y2=Rotation_func(points_x1, points_y1,angle)
    delta=points_x1[len(points_x1)-1]-points_x1[0]
    points_x3,points_y3=Shift_func(points_x2, points_y2,delta)
    points_x4,points_y4=Merge_func(points_x1,points_x3,points_y1, points_y3)
    points_x5,points_y5=Reflection_func(points_x4, points_y4)
    points_x6,points_y6=Merge_func(points_x4,points_x5,points_y4, points_y5)
    points_x=points_x6
    points_y=points_y6
Plot_func(points_x,points_y)


plt.gca().set_aspect('equal', adjustable='box')
plt.show()
