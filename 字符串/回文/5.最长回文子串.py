#!/usr/bin/python3

# -*- encoding:utf-8 -*-

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

def longestPalindrome( s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = []
        res = []
        if len(s)>1000:
            return 'out of limitation'
        for i in range(len(s)):
            for j in range(len(s)-i):
                palindrome.append(s[i:i+j+1]) #所有子串
        for str in palindrome:
            if str == str[::-1] and len(str)>2: #判断是否为回文，长度是否大于2
                res.append(str)
                res.sort(key=lambda str:len(str))
        return res[len(res)-1]

#list index out of range T.T
