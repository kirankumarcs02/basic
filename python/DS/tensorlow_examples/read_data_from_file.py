import tensorflow as tf
import utils
DATA_FILE = "data/birth_file.txt"
# Step 1: read in data from the .txt file
# data is a numpy array of shape (190, 2), each row is a datapoint
data, n_samples = utils.read_birth_life_data(DATA_FILE)
# Step 2: create placeholders for X (birth rate) and Y (life expectancy)
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')
# Step 3: create weight and bias, initialized to 0
w = tf.get_variable('weights', initializer=tf.constant(0.0))
b = tf.get_variable('bias', initializer=tf.constant(0.0))
# Step 4: construct model to predict Y (life expectancy from birth rate)
Y_predicted = w * X + b
# Step 5: use the square error as the loss function
loss = tf.square(Y - Y_predicted, name='loss')
# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)
sess = tf.Session()
# Step 7: initialize the necessary variables, in this case, w and b
sess.run(tf.global_variables_initializer())
# Step 8: train the model
for i in range(100): # run 100 epochs
    for x, y in data:
# Session runs train_op to minimize loss
        sess.run(optimizer, feed_dict={X: x, Y:y})
# Step 9: output the values of w and b
w_out, b_out = sess.run([w, b])

print('w_out', w_out)
print('b_out', b_out)