from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        list_answer = list()

        for i in sorted(intervals, key=lambda x: x[0]):

            if list_answer and i[0] <= list_answer[-1][-1]:
                list_answer[-1][-1] = max(list_answer[-1][-1], i[-1])
            else:
                list_answer.append(i)

        return list_answer

