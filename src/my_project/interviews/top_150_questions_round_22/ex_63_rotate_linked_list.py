from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Edge cases
        if not head or not head.next or k == 0:
            return head
        
        # Find length and last node
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Calculate effective rotations
        k = k % length
        if k == 0:
            return head
        
        # Find new tail (at position length - k - 1)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # New head is next to new tail
        new_head = new_tail.next
        
        # Break the link
        new_tail.next = None
        
        # Connect old tail to old head
        current.next = head
        
        return new_head