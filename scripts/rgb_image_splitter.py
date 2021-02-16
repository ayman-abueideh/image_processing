from matplotlib import pyplot as plt
import matplotlib.image as mpimage
import numpy as np


image_path = "images/NMS.jpg"
image = np.array(mpimage.imread(image_path))

red = np.zeros(image.shape, dtype='uint8')
green = np.zeros(image.shape, dtype='uint8')
blue = np.zeros(image.shape, dtype='uint8')
red[:, :, 0] = image[:, :, 0]
green[:, :, 1] = image[:, :, 1]
blue[:, :, 2] = image[:, :, 2]
images = [image, red, green, blue]

rows = 2
columns = 2

fig = plt.figure(figsize=(20, 20))
for index, sub_image in enumerate(images):
    ax = fig.add_subplot(rows, columns, index + 1)
    ax.imshow(sub_image)
    ax.axis('off')
plt.show()
