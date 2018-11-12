# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj


def matching_KMP(t, p, pnext):
    j, i = 0, 0
    n, m = len(t), len(p)
    result = []
    while j < n and i <= m:
        if i == -1 or t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = pnext[i]
        if i == m:
            result.append(j - i)
            i = 0
    return result


def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


if __name__ == '__main__':
    t = input("输入待匹配字符串：").strip()
    p = input("输入模式串:").strip()
    print("从第一个位置计算， {}位置开始匹配成功"
          .format([x + 1 for x in matching_KMP(t, p, gen_pnext(p))]))
