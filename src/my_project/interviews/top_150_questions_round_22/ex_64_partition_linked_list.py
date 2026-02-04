from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes for the two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        # Pointers to build the two lists
        less = less_dummy
        greater = greater_dummy
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                # Add to the "less than" list
                less.next = current
                less = less.next
            else:
                # Add to the "greater or equal" list
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Important: Set the end of greater list to None
        # to avoid cycles
        greater.next = None
        
        # Connect the two lists
        less.next = greater_dummy.next
        
        # Return the head of the combined list
        return less_dummy.next