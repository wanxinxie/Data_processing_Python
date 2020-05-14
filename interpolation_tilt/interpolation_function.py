# -*- coding: utf-8 -*-

def interpolate_tilt( x_coord, y_coord, thetax,thetay, xStart, xEnd, yStart, yEnd, numRows):
  # Input:
    # x_coord
    # y_coord
    # thetax
    # thetay
    # xStart: the start of x axis of the analyzed area
    # xEnd: the end of x axis of the analyzed area
    # yStart: the start of y axis of the analyzed area
    # yEnd: the end of y axis of the analyzed area
    # numRows: number of rows
  # Output:
    # outZXY: an interpolation of tilt values
  x = np.linspace(xStart, xEnd, int(sqrt(numRows)))
  y = np.linspace(yStart, yEnd, int(sqrt(numRows)))
  X,Y = np.meshgrid(x, y) 

  m,n = X.shape
  R,C = np.mgrid[:m,:n]
  outX = np.column_stack((C.ravel(),R.ravel(), X.ravel()))

  m,n = Y.shape
  R,C = np.mgrid[:m,:n]
  outY = np.column_stack((C.ravel(),R.ravel(), Y.ravel()))

  ZX = interpolate.griddata((x_coord, y_coord), thetax , (X,Y), method='linear')
  ZY = interpolate.griddata((x_coord, y_coord), thetay , (X,Y), method='linear')

  m,n = ZX.shape
  R,C = np.mgrid[:m,:n]
  outZX = np.column_stack((C.ravel(),R.ravel(), ZX.ravel()))
  outZX[:,0] = outX[:,2]
  outZX[:,1] = outY[:,2]

  m,n = ZY.shape
  R,C = np.mgrid[:m,:n]
  outZY = np.column_stack((C.ravel(),R.ravel(), ZY.ravel()))

  outZXY = np.empty([int(numRows) , 4])
  outZXY[:,:3] = outZX
  outZXY[:,3] = outZY[:,2]

  return outZXY

