import cv2
import os.path
import numpy as np
def bluring (image,x1,x2,y1,y2,power):
    image[y1:y2, x1:x2] = cv2.blur(image[y1:y2, x1:x2], (power, power), 0)

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.splitext(name)[0]+"-edit"+os.path.splitext(name)[1],image)

name="out1.png"
image = cv2.imread(name, cv2.IMREAD_COLOR)
bluring(image,10,180,20,30,1000)

viewImage(image, "blured")



