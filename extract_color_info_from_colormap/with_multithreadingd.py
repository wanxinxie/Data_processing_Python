import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

import concurrent.futures
import time

colorbar=plt.imread('colorbar.png')
colorbar = colorbar*255

colorbar = colorbar.astype(int)
colorbar_3 = colorbar[:,25,0:3]

colorbar_3.shape

img=plt.imread('data.png')

img = img*255
img = img.astype(int)
img_3 = img[:,:,0:3]

img_3.shape



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

k=[]
with concurrent.futures.ProcessPoolExecutor() as executor:
    l = [r*10 for r in range(1,138)]
    results = executor.map(matrix_fill, l)

    for result in results:
        k.append(result)

m = np.concatenate([k[i] for i in range(137)], axis=1)

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

def display_cmap(cmap):
    plt.imshow(np.linspace(0, 100, 256)[None, :],  aspect=25,    interpolation='nearest', cmap=cmap) 
    plt.axis('off')

basic_cols=['#4FB2CD', '#3d559e', '#050809','#db3f39', '#fcf051']
my_cmap=LinearSegmentedColormap.from_list('mycmap', basic_cols)
display_cmap(my_cmap)

plt.matshow(final, cmap=my_cmap)
plt.colorbar()

final = matrix/1244*200
final = final-100

