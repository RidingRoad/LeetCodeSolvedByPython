#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = "1.0.0"
__author__ = "RidingRoad <ridingroad@163.com>"

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a _subsequence_ and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        通过"滑动窗口"的思路去解决。使用字典记录字符最后出现的位置，通过判断目前的字符与窗口内容的关系控制窗口大小，使用result记录最大长度
        :param s:
        :return:
        """
        result = 0
        characters_map = {}
        left = -1

        for index, character in enumerate(s):
            if character not in characters_map:
                characters_map[character] = index
            else:
                if left < characters_map[character]:
                    left = characters_map[character]
                characters_map[character] = index
            result = max(result, index - left)

        return result
