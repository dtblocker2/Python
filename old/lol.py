import numpy as np
import matplotlib.pyplot as plt
from math import floor

ax = plt.axes(projection="3d")

'''x=np.arange(0,50,0.1)
y=np.arange(0,50,0.1)
#y=np.sin(x)
z=np.cos(x)'''

x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)

X, Y = np.meshgrid(x, y)

Z=np.cos(X)+np.sin(Y)

ax.plot_surface(X,Y,Z,cmap="Spectral")
plt.show()
