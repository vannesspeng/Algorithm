#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:pyy
# datetime:2019/5/16 15:55

# 两数相加
# 给出两个非空链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的， 并且他们的每个节点智能存储一位数字
# 如果我们将这两个数字相加起来，则会返回一个新的链表来表示它们的和。
# 你可以假设数字0除外，这两个数都不会以0开头

# 示例：
# 输入：(2-> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342

class ListNode():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution():
    def addTwoNumber(self, l1, l2):
        dummyHead = ListNode(0)
        p , q, carry = l1, l2, 0
        curr = dummyHead

        while p != None or q!= None:
            x = p.value if p !=None else 0
            y = q.value if q !=None else 0

            sum = x + y + carry
            carry = int(sum / 10)
            curr.next = ListNode(sum % 10)
            curr = curr.next

            p = p.next if p != None else None
            q = q.next if q !=None else None

        if carry > 0:
            curr.next = ListNode(carry)
        return dummyHead.next

m=[2,4,9]
n=[5,6,4]

def list_to_link(lis):
    listnode_lis = []
    for i in range(0, len(lis)):
        listnode_lis.append(ListNode(lis[i]))
    for i in range(0, len(listnode_lis)-1):
        listnode_lis[i].next = listnode_lis[i+1]
    return listnode_lis[0]


solution = Solution()

x = solution.addTwoNumber(list_to_link(m), list_to_link(n))

while x:
    print(x.value)
    x = x.next





