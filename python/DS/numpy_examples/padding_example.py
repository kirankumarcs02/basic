import numpy as np
import matplotlib.pyplot as plt


a = [1, 2, 3, 4, 5]
pad_a = np.pad(a, (1,3), 'constant', constant_values=(4, 6))
print('constant pad_a = ', pad_a)
pad_a = np.pad(a, (2, 3), 'edge')
print('Edge pad_a = ', pad_a)
pad_a = np.pad(a, (5, 5), 'linear_ramp', end_values=(5, -4))
print('linear_ramp p_a = ', pad_a)
pad_a= np.pad(a, (2,), 'maximum')
print('maximum pad_a= ',pad_a)
pad_a = np.pad(a, (2,), 'mean')
print('mean pad_a = ', pad_a)
pad_a = np.pad(a, (2,), 'median')
print('median pad_a', pad_a)


b = [[1, 2], [3, 4]]
print('b =', b)
pad_b = np.pad(b, (3, 2), 'minimum')
print('pad_b', pad_b)
c = [1,2]
pad_b = np.pad(c, (3, 2), 'linear_ramp', end_values=(5, -4))

print('pad_b = ', pad_b)

np.random.seed(1)
x = np.random.randn(2, 3,2)
x_pad = np.pad(x, ((1,1), (0,0), (0,0)), 'constant', constant_values = (0,0))
y_pad = np.pad(x, ((0,0), (1,1), (0,0)), 'constant', constant_values = (0,0))

z_pad = np.pad(x, ((0,0), (0,0), (1,1)), 'constant', constant_values = (0,0))
print('x =' ,x)
print('x_pad', x_pad)
print('x_pad[0,:,:] = ', x_pad[1,:,:])
print('y_pad', y_pad)
print('z_pad', z_pad)

fig, axarr = plt.subplots(1, 4)
axarr[0].set_title('x')
axarr[0].imshow(x[0,:,:])
axarr[1].set_title('x_pad')
axarr[1].imshow(x_pad[0,:,:])
axarr[2].set_title('y_pad')
axarr[2].imshow(y_pad[0,:,:])
axarr[3].set_title('z_pad')
axarr[3].imshow(z_pad[0,:,:])
plt.show()


x_pad = np.pad(x, ((1,1), (0,0), (0,0)), 'maximum')
print('maximum x_pad =',x_pad)

print('x[0,:,:] = ', x[0,:,:])
print('x[0] = ', x[0])
print('x[:,:,0] = ', x[:,:,0])
