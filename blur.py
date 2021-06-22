import cv2

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread("2.jpg")
cropped = image[10:50, 10:20]
viewImage(cropped, "Пёсик после кадрирования")