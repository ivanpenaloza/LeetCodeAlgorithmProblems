from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dic = OrderedDict()


    def get(self, key: int) -> int:

        if key not in self.dic:
            return -1
        val = self.dic[key]
        self.dic.move_to_end(key)
        return val 

    def put(self, key: int, value: int) -> None:
        
        self.dic[key] = value  
        self.dic.move_to_end(key)

        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)