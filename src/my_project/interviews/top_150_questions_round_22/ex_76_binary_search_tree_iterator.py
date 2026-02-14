from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node: Optional[TreeNode]) -> None:
        """Push all left children of a node onto the stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the top node (next smallest element)
        node = self.stack.pop()
        
        # If it has a right child, push all left descendants of the right child
        if node.right:
            self._push_left(node.right)
        
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        