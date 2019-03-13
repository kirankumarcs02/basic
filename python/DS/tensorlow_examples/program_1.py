import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
writer = tf.summary.FileWriter('./graphs', tf.get_default_graph())
with tf.Session() as sess:
	# writer = tf.summary.FileWriter('./graphs', sess.graph) # if you prefer creating your writer using session's graph
	print(sess.run(x))
writer.close()

#  in terminal try this one
# $ python3 [my_program.py]
# $ tensorboard --logdir="./graphs" --port 6006
# or
# python -m tensorboard.main --logdir="./graphs" --port 6006