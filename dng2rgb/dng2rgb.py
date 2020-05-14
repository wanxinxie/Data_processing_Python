import rawpy
import imageio
import matplotlib.pyplot as plt
from google.colab import files

raw = rawpy.imread('1.dng')
rgb = raw.postprocess()
plt.imshow(rgb)
type(rgb)

imageio.imsave('1.tiff', rgb)
files.download('1.tiff')

raw = rawpy.imread('2.dng')
rgb2 = raw.postprocess()
plt.imshow(rgb2)
type(rgb2)

imageio.imsave('2.tiff', rgb2)
files.download('2.tiff')

raw = rawpy.imread('3.dng')
rgb3 = raw.postprocess()
plt.imshow(rgb3)
type(rgb3)

imageio.imsave('3.tiff', rgb3)
files.download('3.tiff')

