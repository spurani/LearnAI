import cv2

# Black and White (Gray Scale)
img = cv2.imread ("Penguins.jpg",1)

print(img)

resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Penguins", resized_image)

cv2.imWrite("Penguins_resized", resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()