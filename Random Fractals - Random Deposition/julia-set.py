import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import random as rand
import math

nipy_spectral = mpl.colormaps['gist_ncar']
for x in range(100000):
    x=rand.uniform(-2,2)
    y=rand.uniform(-2,2)
    z=complex(x,y)
    c=-0.4+0.6j
    zc=z
    for i in range(7):
        zc=zc*zc+c
    l=math.sqrt(math.pow(zc.real,2)+math.pow(zc.imag,2))
    plt.plot(z.real,z.imag,'ro',markersize=0.5,markeredgecolor=nipy_spectral(math.log(1/l)))
plt.show()