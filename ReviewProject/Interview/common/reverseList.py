#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-22 下午12:16
# @Author  : huiqin
# @File    : reverseList.py
# @Software: PyCharm Community Edition
# @Description : Class is for
class ListNode:
    def __init__(self, x):
        self.val = x;
        self.next = None;


def nonrecurse(head):  # 循环的方法反转链表
    if head is None or head.next is None:
        return head;
    pre = None;
    cur = head;
    h = head;
    while cur:
        h = cur;
        tmp = cur.next;
        cur.next = pre;
        pre = cur;
        cur = tmp;
    return h;


head = ListNode(1);  # 测试代码
p1 = ListNode(2);  # 建立链表1->2->3->4->None;
p2 = ListNode(3);
p3 = ListNode(4);
head.next = p1;
p1.next = p2;
p2.next = p3;
p = nonrecurse(head);  # 输出链表 4->3->2->1->None
while p:
    print p.val;
    p = p.next;


class ListNode:
    def __init__(self, x):
        self.val = x;
        self.next = None;


def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
    if head is None:
        return;
    if head.next is None:
        newhead = head;
    else:
        newhead = recurse(head.next, newhead);
        head.next.next = head;
        head.next = None;
    return newhead;


head = ListNode(1);  # 测试代码
p1 = ListNode(2);  # 建立链表1->2->3->4->None
p2 = ListNode(3);
p3 = ListNode(4);
head.next = p1;
p1.next = p2;
p2.next = p3;
newhead = None;
p = recurse(head, newhead);  # 输出链表4->3->2->1->None
while p:
    print p.val;
    p = p.next;

# 一种比较简单的方法是用“摘除法”。就是先新建一个空节点，然后遍历整个链表，依次令遍历到的节点指向新建链表的头节点。
#那样例来说，步骤是这样的：
# 1. 新建空节点：None
# 2. 1->None
# 3. 2->1->None
# 4. 3->2->1->None
"""
Definition of ListNode

class ListNode(object):

 def __init__(self, val, next=None):
  self.val = val
  self.next = next
"""


class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
        Reverse it in-place.
    """

    def reverse(self, head):
        temp = None
        while head:
            cur = head.next
            head.next = temp
            temp = head
            head = cur
        return temp
        # write your code here

# 还有一种稍微难度大一点的解法。我们可以对链表中节点依次摘链和链接的方法写出原地翻转的代码：
"""
Definition of ListNode

class ListNode(object):

 def __init__(self, val, next=None):
  self.val = val
  self.next = next
"""


class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
        Reverse it in-place.
    """

    def reverse(self, head):
        if head is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = head, head.next
        while cur:
            temp = cur
            # 把摘链的地方连起来
            pre.next = cur.next
            cur = pre.next
            temp.next = dummy.next
            dummy.next = temp
        return dummy.next
        # write your code here
