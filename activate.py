import numpy as np

x = np.array([-1.0, 1.0, 2.0])
def step_func(x):
    y = x > 0
    c=y.astype(np.int32)
    return c

print(step_func(x))
