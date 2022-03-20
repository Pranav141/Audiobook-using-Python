import cv2
image=cv2.imread("C:\\Users\\Pranav\\Desktop\\EXTRACTED_IMAGES\\image_0.png")
half = cv2.resize(image, (0, 0), fx = 0.2, fy = 0.2)
cv2.imshow("Hello",half)
cv2.waitKey()
cv2.destroyAllWindows()
