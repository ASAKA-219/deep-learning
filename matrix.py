import numpy as np

x=np.array([1, 2])
print(x,x.shape)

w = np.array([[1, 3, 5],[2, 4, 6]])
print(w,w.shape)

y = np.dot(x, w) #ここのnp.dotがあるからいちいちかけ算しなくて済む
print(y)
