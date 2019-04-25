#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:pyy
# datetime:2019/3/7 16:49

# 最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
# 最坏时间复杂度：O(n2)
# 稳定性：稳定
alist = [10, 30, 76, 5, 18, 0, 24, 8, 16, 66, 92, 84, 53, 78, 9]

print(alist)

def bubble_sort(alist):
    count = len(alist)
    for i in range(count-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
        print(alist)
    return alist

if "__main__" == __name__:
    print(bubble_sort(alist))