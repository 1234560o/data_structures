# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj


class StackUnderflow(ValueError):
    pass


class SStack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()


if __name__ == "__main__":
    stack = SStack()
    try:
        print(stack.pop())
    except StackUnderflow as e:
        print(e)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.top())
    while not stack.is_empty():
        print(stack.pop())
