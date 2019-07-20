import cv2
cam = cv2.VideoCapture(0)
ret, image = cam.read()
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_red = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow("Gray Image", image)
cv2.imshow(" Image", image_red)

cv2.waitKey(0)