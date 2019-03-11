import tensorflow as tf
import numpy as np

labels = np.array([1,2,3,0,2,1])
one_hot_matrix = tf.one_hot(labels, depth=4, axis=0, name='one_hot_matrix')

one_hot_matrix_2 = tf.one_hot(labels, depth=4, name='one_hot_matrix_2')

one_hot_matrix_3 = tf.one_hot(labels, depth=4, on_value= 4 ,name='one_hot_matrix_3')
sess = tf.Session()
print('one_hot_matrix = ',sess.run(one_hot_matrix))
print('one_hot_matrix_2 = ',sess.run(one_hot_matrix_2))
print('one_hot_matrix_3 = ',sess.run(one_hot_matrix_3))
