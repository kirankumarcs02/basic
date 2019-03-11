import tensorflow as tf

# Initialize two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

print('x1 = ', x1)
print('x2 = ', x2)

# Multiply
result = tf.multiply(x1, x2)

# Print the result
print(result)

# initialize the session
sess = tf.Session()

# Print x1,x2 and  result
print('x1 = ', sess.run(x1))
print('x2 = ', sess.run(x2))
print('result = ',sess.run(result))

# Close the session
sess.close()

# https://github.com/fjospinas/complete-guide-to-tensorflow-for-deep-learning-with-python