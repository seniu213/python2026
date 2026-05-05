import matplotlib.pyplot as plt


x = [1, 3, 5, 7]
y = [27, 30, 21, 29]

plt.plot(x, y, color="green")
plt.grid(True)
plt.xlabel("day")
plt.ylabel("temperature")
plt.title("Temperature plot")
plt.show()
