import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="dataset/italy.jpg", help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

(b, g, r) = image[50, 20]
print("Pixel at (50, 20)", r, g, b)

image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print("Pixel at (20, 50)", r, g, b)

(cX, cY) = (w // 2, h // 2)

tl = image[0:cY, 0:cX]
cv2.imshow("TL", tl)

tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]
cv2.imshow("TR", tr)
cv2.imshow("BR", br)
cv2.imshow("BL", bl)

image[0:int(cY/2), 0:int(cX/2)] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0)