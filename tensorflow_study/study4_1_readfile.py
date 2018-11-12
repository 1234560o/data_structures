# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj

import tensorflow as tf

filename_queue = tf.train.string_input_producer(['stat0.csv', 'stat1.csv'])
reader = tf.TextLineReader()
_, value = reader.read(filename_queue)
record_defaults = [[0], [0], [0.0], [0.0]]
id, age, income, outgo = tf.decode_csv(value, record_defaults=record_defaults)
with tf.Session() as sess:
    print(sess.run(id))
# features = tf.stack([id, age, income, outgo])
