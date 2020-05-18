import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

import concurrent.futures
import time

def matrix_fill(l):
  matrix_2 = np.zeros( (1374,10) )
  for i in range(1374): # a...b-1
    for j in range(l,l+10):#c...d-1
      rgb = img_3[i,j]
      red = rgb[0]
      green = rgb[1]
      blue = rgb[2]
      k = colorbar_3 == rgb
      potential_values = np.where(np.all(k==np.array([True,True,True]),axis=1))
      p = potential_values[0].shape
      idx = p[0]
      if (idx != 0):
        value = potential_values[0][0]
      if (idx == 0):
        distance = []
        for k in range(1244):
          dis = colorbar_3[k] - img_3[i,j]
          d = dis[0]**2 + dis[1]**2 + dis[2]**2
          distance.append(d)
        val, index = min((val, index) for (index, val) in enumerate(distance))
        value = index
      matrix_2[i,j-l] = value
  return matrix_2

