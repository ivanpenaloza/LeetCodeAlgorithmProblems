from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check_mirror(root1=root, root2=root)

    def check_mirror(self, root1: TreeNode, root2: TreeNode):

        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            try:
                root1.val 
                root2.val 
            except:
                return False

            if root1.val != root2.val:
                return False 
            else: 
                return self.check_mirror(root1.left, root2.right) \
                       and self.check_mirror(root1.right, root2.left)
        else:
            return False 

