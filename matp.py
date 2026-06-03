import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.figure(figsize=(6, 4))

plt.plot(x, y)

plt.title("Basic Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)

plt.show()