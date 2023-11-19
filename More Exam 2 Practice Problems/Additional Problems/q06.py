import numpy as np
from matplotlib import pyplot as plt

# P(x) equation
def P(x, u, s):
    return (1 / (np.sqrt(2 * np.pi * s**2))) * np.exp(np.exp(-((x - u)**2) / (2 * s ** 2)))

# Make x and y values
x_values = np.linspace(-3, 3, 1000000)
y_values = P(x_values, 0, 1)

# Plot
plt.title("Very important stat function")
plt.xlabel("x values")
plt.ylabel("P(x) values")

plt.plot(x_values, y_values)
plt.show()