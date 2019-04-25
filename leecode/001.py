#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:pyy
# datetime:2019/4/24 16:48

# 1、两数之和。
# 给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的**两个**整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案，但是你不能重复利用这个数组中同样的元素。
# 示例：
# 给定 nums = [2, 7, 11, 15]， target = 9
# 因为 num[0] + nums[1] = 2 + 7 = 9
# 所以返回[0, 1]



# 第一种暴力法
def getNumIndex(lis, target):
    l = len(lis)
    for i in range(l-1):
        for j in range(i+1, l):
            if lis[i] + lis[j] == target:
                return [i, j]



## 一次Hash
def twoNum(lis, target):
    if len(lis) < 2:
        return False

    dic = {}
    for i in range(len(lis)):
        if nums[i] in dic:
            return [dic[nums[i]], i]
        else:
            dic[target - nums[i]] = i

nums = [2, 7, 11, 15, 98, 88, 900, 9, 45]
target = 9
# print(getNumIndex(nums, target=998))
print(twoNum(nums, target=998))