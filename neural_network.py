# Require tensorflow
# Very initial model
import tensorflow as tf


def Neural_Network(vector_rep, opts = 'train'):
    if opts == 'train':
        train(vector_rep)
        return None
    elif opts == 'test':
        return test(vector_rep)


def train(vector_rep):
    pass


def NN(): # Randomly assuming the dim = 1024, class = 10
    h0 = tf.placeholder(tf.float32, shape=[None, 1024]) # have to fix the size of representation
    w0 = tf.get_variable('w0', [1023, 500], initializer=tf.random_normal_initializer(mean = 0.0 ,stddev= 0.1/(5**2)**(1/2)))
    b0 = tf.get_variable('b0', [500], initializer=tf.constant_initializer(0.01))
    h1 = tf.nn.relu((tf.matmul(h0, w0) + b0))
    w1 = tf.get_variable('w0', [500, 100], initializer=tf.random_normal_initializer(mean = 0.0 ,stddev= 0.1/(5**2)**(1/2)))
    b1 = tf.get_variable('b0', [100], initializer=tf.constant_initializer(0.01))
    h2 = tf.nn.relu((tf.matmul(h1, w1) + b1)
    w2 = tf.get_variable('w0', [100, 10], initializer=tf.random_normal_initializer(mean = 0.0 ,stddev= 0.1/(5**2)**(1/2)))
    b2 = tf.get_variable('b0', [10], initializer=tf.constant_initializer(0.01))
    h3 = tf.nn.relu((tf.matmul(h2, w2) + b2))
    h4 = tf.nn.softmax(h3)
    return h0, h4


def testtest(vector_rep):
    return prediction
