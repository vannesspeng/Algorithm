#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:pyy
# datetime:2019/4/25 11:20
#


# ******2、无重复字符的最长子串的长度？*******
# 给定一个字符串，请你找出其中不含有重复字符的最长子串长度。
# 示例1：
# 输入"abcabcbb" ----输出3
# 解释：因为无重复字符的最大子串是"abc"，所以长度为3
#
# 示例2：
# 输入"bbbbb" ----输出1
# 解释：因为无重复字符的最大子串是"b"，所以长度为1
#
# 示例3：
# 输入"pwwkew" ----输出3
# 解释：因为无重复字符的最大子串是"wke"，所以长度为3
#
# 请注意你的答案必须为子串长度，"pwke"是一个序列，而不是一个子串。
#

s = "pdfgwwfkew"

# hashmap + 滑动窗口
# 时间复杂度:O(n)
class Solution:
    def lengthOfLongestSub(self, s : 'str') -> 'int':
        start = answer = 0
        dic = {}

        for i in range(len(s)):
            if s[i] in dic:
                # start作为滑动窗口的起始位置，是不可以往回走的，当第一次碰碰到w重复时start等于dic['w']+1=5，
                # 滑动窗口继续滑动，喷到f重复了，此时还是同样的计算，start等于等于dic['f']+1=3，明显是不对的，所以这个时候
                # start还是应该取start的初始值
                start = max(start, dic[s[i]] + 1)
            dic[s[i]] = i
            # 元素没有重复的情况answer是取值i-start+1， 当元素重复时，answer取原始值不变
            answer = max(answer, i-start+1)
        return answer
solution = Solution()
print(solution.lengthOfLongestSub(s))


