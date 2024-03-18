import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[0], cmap="Greys")
plt.axis('off') # 軸を非表示にする

plt.savefig('digit_image.png')
plt.show()
