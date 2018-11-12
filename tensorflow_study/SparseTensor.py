# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj

import tensorflow as tf
import numpy

BATCHSIZE = 6
label = tf.expand_dims(tf.constant([0, 2, 3, 6, 7, 9]), 1)
index = tf.expand_dims(tf.range(0, BATCHSIZE), 1)
# use a matrix
concated = tf.concat([index, label], 1)
onehot_labels = tf.sparse_to_dense(concated, [BATCHSIZE, 10], 1, 0)

# use a vector
concated2 = tf.constant([1, 3, 4])
# onehot_labels2 = tf.sparse_to_dense(concated2, tf.pack([BATCHSIZE,10]), 1.0, 0.0)
# cant use ,because output_shape is not a vector
onehot_labels2 = tf.sparse_to_dense(concated2, [10], 1.0, 0.0)  # can use

# use a scalar
concated3 = tf.constant(5)
onehot_labels3 = tf.sparse_to_dense(concated3, [10], 1.0, 0.0)

with tf.Session() as sess:
    result1 = sess.run(onehot_labels)
    result2 = sess.run(onehot_labels2)
    result3 = sess.run(onehot_labels3)
    print("This is result1:")
    print(result1)
    print("This is result2:")
    print(result2)
    print("This is result3:")
    print(result3)
