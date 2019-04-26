#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:pyy
# datetime:2019/4/26 8:56

class Solution():

    # 第一种：使用数学方式从获取数字的个位数开始，逐步构建逆序数
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        is_minus = False
        if x < 0:
            is_minus = True
            x = -x
        while(x):
            temp = x % 10
            res =  res * 10 + temp
            x = int(x / 10)
        res = -res if is_minus else res
        return res if -2 ** 32 < x < 2 ** 32 else 0

    # 第二种：使用Python字符串切片的特性，直接逆向输出逆序数
    def reverse_by_splite(self, x):
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(x)[:0:-1])
        if -2 ** 32 < x < 2 ** 32:
            return result
        else:
            return 0



x = -951082131
solution = Solution()
print(solution.reverse(x))
print(solution.reverse_by_splite(x))