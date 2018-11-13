# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj

import tensorflow as tf

a = tf.constant([[[2, 4], [2, 3], [5, 4]]])
print("a的维度：{}".format(a.shape))
b = tf.constant([[[11, 10], [12, 23], [34, 12]]])
print("b的维度：{}".format(b.shape))
c0 = tf.concat([a, b], 0)
c1 = tf.concat([a, b], 1)
c2 = tf.concat([a, b], 2)
c = tf.concat([a, b], -1)
with tf.Session() as sess:
    print("a的值为：")
    print(sess.run(a))
    print("b的值为：")
    print(sess.run(b))
    print("axis = 0结果为：")
    print(sess.run(c0))
    print("axis = 1结果为：")
    print(sess.run(c1))
    print("axis = 2结果为：")
    print(sess.run(c2))
    print("axis = -1结果为：")
    print(sess.run(c))
