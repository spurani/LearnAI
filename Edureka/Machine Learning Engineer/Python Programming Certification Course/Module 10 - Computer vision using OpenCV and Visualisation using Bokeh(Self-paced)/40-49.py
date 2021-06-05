import cv2

#Black and white(Gray Scale)
img=cv2.imread("Penguins.jpg",0)

cv2.imshow("Penguins",img)

cv2.waitKey(0)

#cv2.waitKey(2000)
cv2.destroyAllWindows()



#slide 46

import cv2

#Black and white(Gray Scale)
img=cv2.imread("Penguins.jpg",0)

resized_image=cv2.resize(img,(650,500))
resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Penguins",resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()



#slide 49
import cv2

#Black and white(Gray Scale)
img=cv2.imread("Penguins.jpg",0)

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Penguins",resized_image)

cv2.imwrite("Penguins_resized",resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

