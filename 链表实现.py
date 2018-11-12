# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj


class Node(object):
    """
    定义节点类
    data:数据
    _next:下一个数据
    """
    def __init__(self, data, _next=None):
        self.data = data
        self._next = _next

    def __repr__(self):
        """
        用来定义Node的字节输出
        """
        return str(self.data)


class ChainTable(object):
    """
    定义链表
    """
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def add(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if not self.head:  # 若链表的头为空
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:  # 当有节点时，新增下一个节点
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print("链表是空的")
            return
        if index < 0 or index >= self.length:
            print("超出索引长度")
            return

        # 删除第一个节点
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        # prev为保存前导节点
        # node为保存当前节点
        # 当j与index相等时就
        # 相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:  # 找到节点后将下一个节点覆盖到本节点
            prev._next = node._next
            self.length -= 1

    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('超出索引长度')
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        if j == index:
            node.data = data

    # 查找一个节点
    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('超出索引长度')
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1
        return node.data

    # 从头到尾打印链表
    def print_chain(self):
        if self.isEmpty():
            print('链表为空')
        num = []
        node = self.head
        while node:
            num.append(node)
            node = node._next
        return num

    # 查找一个节点的索引
    def getIndex(self, data):
        j = 0
        if self.isEmpty():
            print('链表为空')
            return
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1
        if j == self.length:
            print("%s not found" % str(data))
            return

    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print('链表为空')
            return
        if index < 0 or index >= self.length:
            print('超出索引长度')
            return
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1
        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "链表为空"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("超出索引长度")
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("超出索引长度")
            return
        self.update(ind, val)

    def __len__(self):
        return self.length


chainTable = ChainTable()
for i in range(10):
    chainTable.add(i)
print(chainTable.getIndex(1))
print(chainTable.print_chain())
print(repr(chainTable))
