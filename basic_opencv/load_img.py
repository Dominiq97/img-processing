import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

print("w:", w)
print("h:",h)
print("channels:",c)

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite("copy.jpg", image)