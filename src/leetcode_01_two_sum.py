#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = "1.0.0"
__author__ = "RidingRoad <ridingroad@163.com>"

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    @staticmethod
    def two_sum(source_list: list, target: int):
        # record the relationship between value and index from source_list
        #  and try to finding the answer at the same time
        value_index_map = {}
        for index, value in enumerate(source_list):
            diff = target - value
            if diff in value_index_map.keys() and index != value_index_map[diff]:
                return [index, value_index_map[diff]]
            value_index_map[value] = index
        return []


if __name__ == '__main__':
    print(Solution.two_sum([2, 7, 11, 15], 9))
