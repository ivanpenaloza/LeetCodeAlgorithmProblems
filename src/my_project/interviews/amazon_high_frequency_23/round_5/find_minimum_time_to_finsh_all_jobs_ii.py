from typing import List, Union, Collection, Mapping, Optional, Dict
from abc import ABC, abstractmethod
import math

class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:

        jobs.sort()
        workers.sort()

        return max([math.ceil(n/d) for n, d in zip(jobs, workers)])
        
