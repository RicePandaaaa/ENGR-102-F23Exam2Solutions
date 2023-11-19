import numpy as np
from matplotlib import pyplot as plt

# Make our function
def P(x, u, s):
    """ Calculates the y value given these parameters """

    y = (1 / np.sqrt(2 * np.pi * s ** 2)) * np.exp(-((x - u) ** 2 / (2 * s **2)))
    return y

# Make our x and y values
x_values = np.linspace(-3, 3, 100)
y_values = P(x_values, 0, 1)

# Make the plot
plt.plot(x_values, y_values)

# Add in stylish elements
plt.title("Question 1")
plt.xlabel("x values")
plt.ylabel("Result of P(x)")
plt.show()
