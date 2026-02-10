import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_72_flatten_binary_tree_to_linked_list import Solution, TreeNode


class FlattenBinaryTreeToLinkedListTestCase(unittest.TestCase):

    def build_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """Build tree from level-order list representation."""
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Add left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            # Add right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root

    def tree_to_array(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        """Convert flattened tree to array format."""
        result = []
        current = root
        
        while current:
            result.append(current.val)
            result.append(current.left)  # Should always be None
            current = current.right
        
        return result

    def test_example_1(self):
        """
        Input: root = [1,2,5,3,4,null,6]
        Output: [1,null,2,null,3,null,4,null,5,null,6]
        """
        solution = Solution()
        root = self.build_tree([1, 2, 5, 3, 4, None, 6])
        solution.flatten(root)
        output = self.tree_to_array(root)
        expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6, None]
        self.assertEqual(output, expected)

    def test_example_2(self):
        """
        Input: root = []
        Output: []
        """
        solution = Solution()
        root = self.build_tree([])
        solution.flatten(root)
        output = self.tree_to_array(root)
        expected = []
        self.assertEqual(output, expected)

    def test_example_3(self):
        """
        Input: root = [0]
        Output: [0]
        """
        solution = Solution()
        root = self.build_tree([0])
        solution.flatten(root)
        output = self.tree_to_array(root)
        expected = [0, None]
        self.assertEqual(output, expected)