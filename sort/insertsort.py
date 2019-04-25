#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:pyy
# datetime:2019/3/12 9:40

# 最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
# 最坏时间复杂度：O(n2)
# 稳定性：稳定
alist = [10, 30, 76, 5, 18, 0, 24, 8, 16, 66, 92, 84, 53, 78, 9]

print(alist)

def insert_sort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
        print(alist)

    return alist

print(insert_sort(alist))