def plot_interpolation(X, Y, ZX, ZY, outZXY, figsizex, figsizey):
    # Input:
      # X: Coordinate matrices from x vectors.
      # Y: Coordinate matrices from y vectors.
      # ZX: Interpolate (x,y,z) points [mat] over a normal (x,y) grid [X,Y]
      # ZY: Interpolate (x,y,z) points [mat] over a normal (x,y) grid [X,Y]
      # outZXY: Combination of the interpolatation on ZX and ZY 
      # figsizex: figsize x value for the predicted interpolation plot
      # figsizey: figsize x value for the predicted interpolation plot
    # Output:
      # plot of Interpolation (x-component)
      # plot of Interpolation (y-component)
      # plot of Interpolation (predicted)
  plt.pcolormesh(X,Y,ZX)
  plt.colorbar()
  plt.show()
  plt.title('ZX: Interpolate (x,y,z) points [mat] over a normal (x,y) grid [X,Y]')

  plt.pcolormesh(X,Y,ZY)
  plt.colorbar()
  plt.show()
  plt.title('ZY: Interpolate (x,y,z) points [mat] over a normal (x,y) grid [X,Y]')

  fig = figure(num=None, figsize=(figsizex, figsizey), dpi=300, facecolor='w', edgecolor='k')
  color_array = np.sqrt((outZXY[:,2]**2 + outZXY[:,3]**2))
  plt.quiver(outZXY[:,0],outZXY[:,1],outZXY[:,2],outZXY[:,3], color_array)
  plt.colorbar()
  plt.show()
