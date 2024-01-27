import numpy as np
import matplotlib.pyplot as plt

def Rotation_func(points):
    points_n=points.copy()
    for x in range(len(points)):
        points_n[x][0]=-(points[x][1]-points[len(points)-1][1])+points[len(points)-1][0]
        points_n[x][1]=(points[x][0]-points[len(points)-1][0])+points[len(points)-1][1]
    points_n=np.flip(points_n, axis=0)
    return  points_n
#rotates shape about last point pi/2 radians

def Plot_func(points):
    for x in range(len(points)):
        if x+1<len(points):
            if x<len(points)/2+1:
                plt.plot([points[x][0],points[x+1][0]],[points[x][1],points[x+1][1]],color="blue")
            if x>=len(points)/2:
                plt.plot([points[x][0],points[x+1][0]],[points[x][1],points[x+1][1]],color="red")
#given a set of points, plots respective lines with each two. the first half is blue and the second is red 
            
points =np.array([ [0,0],[1,0]])
num=8
for x in range(num):
    points_1=Rotation_func(points.copy())
    newpoints=np.concatenate((points,points_1),axis=0)
    points=newpoints

Plot_func(points)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()