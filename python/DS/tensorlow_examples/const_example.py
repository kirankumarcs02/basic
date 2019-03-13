import tensorflow as tf

# tf.constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
# constant of 1d tensor (vector)
a = tf.constant([2, 2], name="vector")
sess = tf.Session()
print('a = ',sess.run(a))

b = tf.constant([[0, 1], [2, 3]], name="matrix")
print('b = ', sess.run(b))


# tf.zeros(shape, dtype=tf.float32, name=None)
# create a tensor of shape and all elements are zeros
c = tf.zeros([2, 3], tf.int32)
print('c = ', sess.run(c))

# tf.zeros_like(input_tensor, dtype=None, name=None, optimize=True)
# create a tensor of shape and type (unless type is specified) as the input_tensor but all elements are zeros.
# input_tensor [[0, 1], [2, 3]]
input_tensor = b
d = tf.zeros_like(input_tensor)
print('d = ', sess.run(d))

# tf.ones(shape, dtype=tf.float32, name=None)
# create a tensor of shape and all elements are ones
e = tf.ones([2, 3], tf.int32)
print('e =', sess.run(e))

# tf.ones_like(input_tensor, dtype=None, name=None, optimize=True)
# create a tensor of shape and type (unless type is specified) as the input_tensor but all elements are ones.
# input_tensor is [[0, 1], [2, 3]]
input_tensor = b
f = tf.ones_like(input_tensor)
print('f = ', sess.run(f))

# tf.fill(dims, value, name=None)
# create a tensor filled with a scalar value.
g = tf.fill([2, 3], 9)
print('g = ', sess.run(g))

# tf.lin_space(start, stop, num, name=None)
# create a sequence of num evenly-spaced values are generated beginning at start. If num > 1, the values in the sequence increase by (stop - start) / (num - 1), so that the last one is exactly stop.
# comparable to but slightly different from numpy.linspace

linspace = tf.lin_space(1.0, 4.0, 4, name="linspace")
print('linspace = ', sess.run(linspace))

# tf.range([start], limit=None, delta=1, dtype=None, name='range')
# create a sequence of numbers that begins at start and extends by increments of delta up to but not including limit
# slight different from range in Python

# 'start' is 3, 'limit' is 18, 'delta' is 3
start = 2
limit = 20
delta = 2
print('range(2,20,2) = ', sess.run(tf.range(start, limit, delta)))
start = 20
limit = 2
delta = -2
print('reange(20,2,-2) = ', sess.run(tf.range(start, limit, delta)))
limit =5
print('range(5)',sess.run(tf.range(limit)))
