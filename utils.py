import matplotlib.pyplot as plt
import math


def plot_images(images):
    rows = math.ceil(math.sqrt(len(images)))
    columns = math.ceil(len(images) / rows)
    fig = plt.figure(figsize=(20, 20))
    for index, sub_image in enumerate(images):
        ax = fig.add_subplot(rows, columns, index + 1)
        ax.imshow(sub_image,cmap="gray")
        ax.axis('off')
    plt.show()
