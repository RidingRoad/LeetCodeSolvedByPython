#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = "1.0.0"
__author__ = "RidingRoad <ridingroad@163.com>"

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        # current_node: 标志当前节点
        current_node = None
        list_node1 = l1
        list_node2 = l2
        # carry: 进位标志位
        carry = 0

        # 当两个链表的节点都遍历完，才退出循环
        while list_node1 or list_node2:
            val = (list_node1.val if list_node1 else 0) + (list_node2.val if list_node2 else 0) + carry
            carry = 1 if val >= 10 else 0
            current_node = list_node1 if list_node1 else list_node2
            val = val % 10
            current_node.val = val
            list_node1 = list_node1.next if list_node1 else None
            list_node2 = list_node2.next if list_node2 else None
            current_node.next = list_node1 if list_node1 else list_node2

        if carry:
            current_node.next = ListNode(1)

        return l1


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    Solution.add_two_numbers(l1, l2)
    print(l1.val, l1.next.val, l1.next.next.val)
