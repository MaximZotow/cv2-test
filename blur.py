import cv2
import os.path
def bluring (image,x1,x2,y1,y2,power):
    image[y1:y2, x1:x2] = cv2.blur(image[y1:y2, x1:x2], (power, power), 0)

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(name_of_window+".png",image)
def blurimage(image):
    img2gray = cv2.cvtColor(image[0:50, 0:200], cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(img2gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))

    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    contour, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        x, y, w, h = cv2.boundingRect(cnt)
        bluring(image, x, x + w, y, y + h, 1000)


name="out1.png"
image = cv2.imread(name, cv2.IMREAD_COLOR)
viewImage(image,"image1")
blurimage(image)
viewImage(image,"image2")



