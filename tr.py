import cv2
import numpy as np
from pyzbar import pyzbar

img = cv2.imread("qtst.png")

decodedObjects = pyzbar.decode(img)

print(decodedObjects)
