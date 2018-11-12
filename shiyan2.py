# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj

n = int(input())
result = []
for i in range(n):
    result.append(list(map(int, input().split())))
count = 0
for i in range(n - 1):
    for j in range(n - i - 1):
        if result[i + j + 1][0] <= result[i][0] and result[i + j + 1][1] >= result[i][1]:
            count += 1
            break
print(count)
