from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        answer = dict()

        for k, v in enumerate(nums):

            if v in answer:
                return [answer[v], k]
            else: 
                answer[target - v] = k

        return []