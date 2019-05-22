import tensorflow as tf
import tensorflow.contrib.eager as tfe

# without enable_eager_execution()
# x = [[4.]]
# m = tf.matmul(x, x)
# print(m) # output Tensor("MatMul:0", shape=(1, 1), dtype=float32)
# with tf.Session() as sess:
#     m_out = sess.run(m)
# print(m_out) #[[16.]]

tfe.enable_eager_execution()

x = [[4.]]
m = tf.matmul(x, x)
print(m) #output tf.Tensor([[16.]], shape=(1, 1), dtype=float32)