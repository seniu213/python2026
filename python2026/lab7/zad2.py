import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 10)
y = np.linspace(0, 25, 10)

plt.scatter(x, y, color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.text(x[0], y[0], "(0,0)")
plt.text(x[-1], y[-1], "(5,25)")
plt.show()
