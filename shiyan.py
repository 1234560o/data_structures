# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj

import math


def function(array):
    for i in range(len(array) - 1):
        if array[i] * array[i+1] <= 0:
            return array[i] if -array[i] <= array[i+1] else array[i + 1]
        if i == len(array) - 2:
            return array[0] if array[0] > 0 else array[i + 1]


print(function([-2, -1.7, 0, 1, 3, 9, 10]))
