import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [10, 20, 30, 40]
y2 = [15, 18, 35, 38]

plt.plot(x, y1, marker='o', label="Dataset 1")
plt.plot(x, y2, marker='s', label="Dataset 2")

plt.title("Comparison Using Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)

plt.show()