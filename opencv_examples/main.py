# importing cv2
import cv2


path = r'/home/mert/PycharmProjects/opencv_examples/elma.jpg'

image = cv2.imread(path,0)

window_name = 'image'

cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()