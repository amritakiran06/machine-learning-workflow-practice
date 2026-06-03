import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperature = [30, 32, 31, 35, 36]

plt.figure()

plt.plot(days, temperature, marker='o', linestyle='-', label="Temperature")

plt.title("Temperature Variation")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

plt.show()