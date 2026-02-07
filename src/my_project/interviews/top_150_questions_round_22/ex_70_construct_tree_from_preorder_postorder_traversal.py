from typing import List, Union, Collection, Mapping, Optional
from abc import ABC, abstractmethod

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap for quick lookup of indices in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.postorder_idx = len(postorder) - 1
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct the tree
            if left > right:
                return None
            
            # Pick the current root from postorder (from end)
            root_val = postorder[self.postorder_idx]
            root = TreeNode(root_val)
            
            # Move to the previous element in postorder
            self.postorder_idx -= 1
            
            # Find the index of root in inorder to split left and right subtrees
            inorder_idx = inorder_map[root_val]
            
            # Build right subtree first (postorder: left → right → root)
            # So when we go backwards, we process root → right → left
            root.right = build(inorder_idx + 1, right)
            
            # Build left subtree
            root.left = build(left, inorder_idx - 1)
            
            return root
        
        return build(0, len(inorder) - 1)