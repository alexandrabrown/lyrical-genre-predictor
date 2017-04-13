# Require tensorflow
# Very initial model
import tensorflow as tf
import numpy as np
from NN.config import get, is_file_prefix


def neural_network(train_matrix, test_matrix, train_truth):
    train_label = one_hot(train_truth)
    train(train_matrix, train_label)
    predicted_test_categories = test(test_matrix)
    return predicted_test_categories

def one_hot(train_truth):
    num_train_data = len(train_truth)
    classs_num = get('MODEL.CLASS_DIM')
    one_hot_vec = np.zeros([num_train_data, classs_num])
    categories = ["Pop", "Rock", "Country", "Blues", "Rap"]
    for i in range(num_train_data):
        class_idx = categories.index(train_truth[i])
        one_hot_vec[i, class_idx] = 1
    return one_hot_vec

def report_training_progress(batch_index, input_layer, loss_func, faces):
    ''' Update user on training progress '''
    if batch_index % 5:
        return
    print('starting batch number %d \033[100D\033[1A' % batch_index)
    if batch_index % 50:
        return
    #error = loss_func.eval(feed_dict={input_layer: faces.test.images, true_labels: faces.test.labels})
    #acc = accuracy.eval(feed_dict={input_layer: faces.test.images, true_labels: faces.test.labels})
    #print('\n \t cross_entropy is about %f' % error)
    #print(' \t accuracy is about %f' % acc)

"""
Batch Gradient Descent
"""
def BGD(input, prediction, true_labels, keep_prob, cross_entropy, optimizer, train_matrix, train_label):
    try:
        curr_idx = 0

        batch_size =  get('TRAIN.NN.NB_STEPS')
        prob = get('TRAIN.NN.DROPOUT_RATE')
        for batch_index in range(get('TRAIN.NN.NB_STEPS')):
            #report_training_progress(batch_index, input_layer, loss_func, faces)
            if curr_idx+batch_size >= len(train_label):
                second_idx = curr_idx+batch_size-len(train_label)
                batch_matrix = np.concatenate((train_matrix[curr_idx:len(train_label),:], train_matrix[:second_idx,:]),axis =0)
                batch_labels = np.concatenate((train_label[curr_idx:len(train_label), :], train_label[:second_idx, :]), axis=0)
            else:
                batch_matrix = train_matrix[curr_idx:curr_idx+batch_size,:]
                batch_labels = train_label[curr_idx:curr_idx+batch_size,:]
            #print(batch_matrix.shape)
            #print(batch_labels.shape)
            optimizer.run(feed_dict={input: batch_matrix, true_labels: batch_labels, keep_prob: prob})
            curr_idx += batch_size
            if curr_idx >= len(train_label):
                curr_idx-=len(train_label)
    except KeyboardInterrupt:
        print('Finish Training')

def get_weights(saver, sess):
    ''' load model weights if they were saved previously '''
    if is_file_prefix('TRAIN.NN.CHECKPOINT'):
        saver.restore(sess, get('TRAIN.NN.CHECKPOINT'))
        print('I restored weights from a saved model!')
    else:
        print('OK, I did not find a saved model, so I will start training from scratch!')


def model(input_dim, class_num): # Randomly assuming the dim = 1024, class = 10
    keep_prob = tf.placeholder(tf.float32)
    h0 = tf.placeholder(tf.float32, shape=[None, input_dim])  # have to fix the size of representatio
    w0 = tf.get_variable('w0', [input_dim, 500], initializer=tf.random_normal_initializer(mean = 0.0 ,stddev= 0.1/(5**2)**(1/2)))
    b0 = tf.get_variable('b0', [500], initializer=tf.constant_initializer(0.01))
    h1 = tf.nn.relu((tf.matmul(h0, w0) + b0))
    w1 = tf.get_variable('w1', [500, 100], initializer=tf.random_normal_initializer(mean = 0.0 ,stddev= 0.1/(5**2)**(1/2)))
    b1 = tf.get_variable('b1', [100], initializer=tf.constant_initializer(0.01))
    h2 = tf.nn.relu(tf.matmul(h1, w1) + b1)
    h2 = tf.nn.dropout(h2, keep_prob)
    w2 = tf.get_variable('w2', [100, class_num], initializer=tf.random_normal_initializer(mean = 0.0 ,stddev= 0.1/(5**2)**(1/2)))
    b2 = tf.get_variable('b2', [class_num], initializer=tf.constant_initializer(0.01))
    h3 = tf.nn.relu((tf.matmul(h2, w2) + b2))
    h4 = tf.nn.softmax(h3)
    return h0, keep_prob, h4


def train(train_matrix, train_label):
    input_dim = train_matrix.shape[1]
    class_num = get('MODEL.CLASS_DIM')
    
    # set up sessions
    sess = tf.InteractiveSession()
    classs_num = get('MODEL.CLASS_DIM')
    input, keep_prob, prediction = model(input_dim, class_num)
    true_labels = tf.placeholder(tf.int64, shape=[None, classs_num])
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = prediction, labels = true_labels))
    correct_prediction = tf.equal(tf.arg_max(prediction, 1), tf.arg_max(train_label, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    optimizer = tf.train.AdamOptimizer(get('TRAIN.NN.LEARNING_RATE')).minimize(cross_entropy)
    
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    
    # load model weights if they were saved previously
    get_weights(saver, sess)
    BGD(input, prediction, true_labels, keep_prob, cross_entropy, optimizer, train_matrix,train_label)
    saver.save(sess, get('TRAIN.NN.CHECKPOINT'))

                    
def test(test_matrix):
    tf.reset_default_graph() # Clear the model first
    categories = ["Pop", "Rock", "Country", "Blues", "Rap"]
    prediction_ls = []
    input_dim = test_matrix.shape[1]
    #print(input_dim)
    class_num = get('MODEL.CLASS_DIM')
                    
    assert is_file_prefix('TRAIN.NN.CHECKPOINT') # Check wether model exists or not
    sess = tf.InteractiveSession()
    input, keep_prob, prediction = model(input_dim, class_num)
    saver = tf.train.Saver()
    saver.restore(sess, get('TRAIN.NN.CHECKPOINT'))
    output = prediction.eval(feed_dict={input: test_matrix, keep_prob: 1})
    prediction_idx = np.argmax(output, axis = 1)
    #print(prediction_idx)
                    
    for i in prediction_idx:
        prediction_ls.append(categories[i])
    
    return prediction_ls




