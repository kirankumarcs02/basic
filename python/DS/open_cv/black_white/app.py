import cv2

# originalImage = cv2.imread('videoplayback.mp4')
# grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
#
# (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
#
# cv2.imshow('Black white image', blackAndWhiteImage)
# cv2.imshow('Original image', originalImage)
# cv2.imshow('Gray image', grayImage)

cap = cv2.VideoCapture('videoplayback.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()