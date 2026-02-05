import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_66_maximum_depth_binary_tree import Solution, TreeNode

class MaximumDepthBinaryTreeTestCase(unittest.TestCase):

    def create_binary_tree(self, values):
        """
        Helper function to create a binary tree from a list of values (level-order).
        
        :param values: List of node values (None represents null nodes)
        :return: Root of the binary tree
        """
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root

    def test_example_1(self):
        # Example 1: Input: root = [3,9,20,null,null,15,7]
        # Output: 3
        solution = Solution()
        root = self.create_binary_tree([3, 9, 20, None, None, 15, 7])
        result = solution.maxDepth(root)
        self.assertEqual(result, 3)

    def test_example_2(self):
        # Example 2: Input: root = [1,null,2]
        # Output: 2
        solution = Solution()
        root = self.create_binary_tree([1, None, 2])
        result = solution.maxDepth(root)
        self.assertEqual(result, 2)