import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="dataset/italy.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

M = np.float32([[1, 0, 40], [0, 1, 60]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("DownRight", shifted)

M = np.float32([[1, 0, -10], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("UpLeft", shifted)

shifted = imutils.translate(image, 0, 80)
cv2.imshow("Down", shifted)
cv2.waitKey(0)
