import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

# Cargar el dataset MNIST
ds = tfds.load('mnist', split='train')


for i, ex in enumerate(ds.take(4)):
    image, label = ex["image"], ex["label"]

    plt.subplot(1, 4, i + 1)
    plt.imshow(image.numpy().squeeze(), cmap='gray')
    plt.title(f'Label: {label.numpy()}')
    plt.axis('off')

plt.show()
