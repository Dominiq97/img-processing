import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="dataset/italy.jpg",
	help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

face = image[100:300, 100:300]
cv2.imshow("Face", face)
cv2.waitKey(0)

body = image[0:500, 0:400]
cv2.imshow("Body", body)
cv2.waitKey(0)