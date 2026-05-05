import numpy as np
import matplotlib.pyplot as plt


x = np.random.randn(10000)
counts, bins = np.histogram(x, bins=10)
centers = (bins[:-1] + bins[1:]) / 2

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.hist(x, bins=10)
plt.subplot(1, 2, 2)
plt.bar(centers, counts, width=bins[1] - bins[0])
plt.show()
