import numpy as np

def squared_error(t, y):
    return 0.5 * np.sum((y - t)**2)

def cross_entropy_error(t, y):
    plus = 0.00000000000000000003
    return -np.sum(t * np.log(y + plus))

y=[0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
t=[0,0,1,0,0,0,0,0,0,0]
l=cross_entropy_error(np.array(t), np.array(y))
k=squared_error(np.array(t), np.array(y))
print(l)
