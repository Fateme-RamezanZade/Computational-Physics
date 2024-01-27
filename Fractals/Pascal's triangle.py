import numpy as np
import matplotlib.pyplot as plt

def tri_construct(num):
    points=np.array([0 for x in range(num)])
    points=np.array([points for x in range(num)])
    for j in range(num):
        points[j][0]=1
        points[j][j]=1
        for i in range(j):
            points[j][i]=points[j-1][i]+points[j-1][i-1]
    return points
#constructs a pascal triangle with (number) rows

def coords_construct(num):
    coords=np.array([0 for x in range(2)])
    coords=np.array([coords for x in range(num)])
    coords=np.array([coords for x in range(num)])
    for j in range(num):
        for i in range(num):
            for k in range(2):
                coords[j][i][1]=100-j
                if i<=j:
                    coords[j][i][0]=i-j+i
    return coords
#constructs points which shape an equilateral triangle in plane

def plot_dots(points,coords,num):
    for j in range(num):
        for i in range(num):
            if points[j][i]!=0:
                if points[j][i]%2==0:
                    plt.scatter([coords[j][i][0]], [coords[j][i][1]], color="red")
                if points[j][i]%2!=0:
                    plt.scatter([coords[j][i][0]], [coords[j][i][1]], color="green")
#plots coordinates of nonzero. green if odd and red if even.

num=32
points=tri_construct(num)
coords=coords_construct(num)
plot_dots(points,coords,num)
plt.axis('off')
plt.show()