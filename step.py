import numpy as np
import matplotlib.pyplot as plt

def sigmoid_func(x):
    return  1/(1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid_func(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
