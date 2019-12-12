import matplotlib.pyplot as plt
import numpy as np

plt.quiver(0,0,2,2,scale_units= 'xy', angles='xy', scale=1)
plt.xlim(-5,5)
plt.ylim(-5,5)
# plt.show()


##########################
a = np.asarray([9, 2])
b = np.asarray([-5, 4])
a_b = np.dot(a,b)/ np.linalg.norm(b)

mul_vec = (a_b/ np.linalg.norm(b)) * b
print(mul_vec)