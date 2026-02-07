import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_70_construct_tree_from_preorder_postorder_traversal import Solution, TreeNode

class ConstructTreeFromPreorderPostorderTestCase(unittest.TestCase):

    def tree_to_list(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        """Convert tree to level-order list representation with None for missing nodes."""
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        
        return result

    def test_example_1(self):
        """
        Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
        Output: [3,9,20,null,null,15,7]
        """
        solution = Solution()
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]
        output = solution.buildTree(inorder, postorder)
        expected = [3, 9, 20, None, None, 15, 7]
        self.assertEqual(self.tree_to_list(output), expected)

    def test_example_2(self):
        """
        Input: inorder = [-1], postorder = [-1]
        Output: [-1]
        """
        solution = Solution()
        inorder = [-1]
        postorder = [-1]
        output = solution.buildTree(inorder, postorder)
        expected = [-1]
        self.assertEqual(self.tree_to_list(output), expected)