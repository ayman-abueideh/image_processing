from matplotlib import pyplot as plt
import matplotlib.image as mpimage
import numpy as np
from skimage import transform as tf
import math


image_path = "../images/normal_board.png"
image = np.array(mpimage.imread(image_path))

dst = np.array(
    [[375, 144], [242, 209], [505, 209], [119, 267], [616, 269], [155, 311], [584, 312], [237, 408], [499, 409]])
src = np.array(
    [[68, 59], [289, 70], [66, 286], [430, 74], [75, 423], [427, 146], [150, 423], [427, 284], [287, 420]])
tform3 = tf.ProjectiveTransform()
tform3.estimate(src, dst)
warped = tf.warp(image, tform3, output_shape=(793, 442))

images = [image, warped]
fig, ax = plt.subplots(nrows=2, figsize=(8, 3))

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].plot(dst[:, 0], dst[:, 1], '.r')
ax[1].imshow(warped, cmap=plt.cm.gray)

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
