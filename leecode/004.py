#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:pyy
# datetime:2019/4/29 9:53

###4、最长回文字子串
# 给定一个字符串s，找到s中最长的回文子串，你可以假设s的最大长度为100。
# > 示例1：
# 输入："babad"
# 输出：bab
# 注意："aba"也是一个有效答案
#
# > 示例2:
# 输入："cbbd"
# 输出："bb"

def manacher(s : str):
    #预处理
    s='#'+'#'.join(s)+'#'

    RL=[0]*len(s)
    MaxRight=0
    pos=0
    MaxLen=0
    for i in range(len(s)):
        # 如果i处于已知最长回文，触及的最右边界， 那么它的取值有两种情况，一种是关于已知pos的对称点的RL[2*pos-i]， MaxRight-i
        if i<MaxRight:
            RL[i]=min(RL[2*pos-i], MaxRight-i)
        else:
            # i在MaxRight的右边，这个时候，没有任何遍历过的回文串可用，只能从自身开始扩展
            RL[i]=1
        #尝试扩展，注意处理边界
        while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
            RL[i]+=1
        #更新MaxRight,pos
        if RL[i]+i-1>MaxRight:
            MaxRight=RL[i]+i-1
            pos=i
        #更新最长回文串的长度
        MaxLen=max(MaxLen, RL[i])
    start = RL.index(MaxLen) - MaxLen + 1
    end = RL.index(MaxLen) + MaxLen
    sub_target_str = s[start:end]
    return sub_target_str.replace("#", "")

s = "cbbddb"
print(manacher(s))