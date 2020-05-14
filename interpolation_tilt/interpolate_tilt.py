import pandas as pd
from numpy import *
from numpy.polynomial import polynomial as pl
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
from math import sqrt

xy = pd.read_csv("wanxin_xy_theta.csv")

y_coord = xy.iloc[:,0:1]
x_coord = xy.iloc[:,1:2]
theta_y = xy.iloc[:,2:3]
theta_x = xy.iloc[:, 3:4]

theta_x = np.asarray(theta_x, dtype=np.float32)
theta_y = np.asarray(theta_y, dtype=np.float32)
x_coord = np.asarray(x_coord)
y_coord = np.asarray(y_coord)

thetax = theta_x.reshape(-1)
thetay = theta_y.reshape(-1)
xcoord = x_coord.reshape(-1)
ycoord = y_coord.reshape(-1)

outZXY_1 = interpolate_tilt(x_coord=xcoord,y_coord=ycoord, thetax=thetax, thetay=thetay, yStart=11370,yEnd=12000, xStart=4920,xEnd=5550, numRows=576)
