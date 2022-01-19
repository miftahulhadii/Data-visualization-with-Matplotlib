import matplotlib.pyplot as hadi #a library for plotting

from matplotlib import cm #a library for colormapping
from mpl_toolkits.mplot3d import Axes3D #a library for plotting in 3D

fig = hadi.figure() #uses to create a canvas for plotting
ax = Axes3D(fig)    #to use a canvas with 3D axis

x = [] #input your Longitude data
y = [] #input your Latitude data 
z = [] #input your Elevation data

#give an instruction to create a plot from available data and select the color mapping
surf = ax.plot_trisurf(x, y, z, cmap='terrain', linewidth=0.1);
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_zlim(-2200, 2200) #give an instruction to limit the z-axis for better view

#create a label in every axis
ax.set_xlabel('Longitude (m)')
ax.set_ylabel('Latitude (m)')
ax.set_zlabel('Elevation (m)')

#give an instruction to show a plot
hadi.show()
