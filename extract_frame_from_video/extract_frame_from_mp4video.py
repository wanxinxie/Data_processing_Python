

import numpy as np
import cv2 as cv
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import scipy.misc
from google.colab import files
import matplotlib.pyplot as plt

cap = cv.VideoCapture('Big_Buck_Bunny_1080_10s_1MB.mp4')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

hsv = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    h = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv.append(h)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

length = len(hsv)

for i in range(length):
  name = 'frame' + str(i) + '.tiff'
  plt.imshow(hsv[i])
  plt.savefig(name, transparent=True, dpi=300, bbox_inches="tight", pad_inches=0.0)
  files.download(name)
