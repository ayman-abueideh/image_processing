import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from utils import plot_images


#
#
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


#
#
# def gray2BW(img, threshold):
#     rows, columns = img.shape
#     bw_image = np.zeros(img.shape, dtype='uint8')
#     bw_image[:] = img[:]
#     for i in range(rows):
#         for j in range(columns):
#             if bw_image[i][j] > threshold:
#                 bw_image[i][j] = 255
#             else:
#                 bw_image[i][j] = 0
#     return bw_image
#
#
np.int
image_path = "../images/NMS.jpg"
img = mpimg.imread(image_path)
img = img.astype('uint32')
gray = rgb2gray(img)
old_image = np.zeros(gray.shape, dtype='b')
old_image[:, :] = gray[:, :]

# bw_image = gray2BW(gray, 210)
images = [old_image, gray]
plot_images(images)
# plt.imshow(img, cmap='gray')
# plt.show()
import cv2
#
originalImage = cv2.imread(image_path)
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
# (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('Black white image', blackAndWhiteImage)
# cv2.imshow('Original image', originalImage)
# cv2.imshow('Gray image', grayImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
