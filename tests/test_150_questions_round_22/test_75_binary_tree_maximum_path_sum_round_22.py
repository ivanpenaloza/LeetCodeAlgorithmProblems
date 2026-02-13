import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_75_binary_tree_maximum_path_sum import Solution, TreeNode


class BinaryTreeMaximumPathSumTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Input: root = [1,2,3]
        Output: 6
        Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
        """
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.maxPathSum(root=tree)
        self.assertEqual(output, 6)

    def test_example_2(self):
        """
        Input: root = [-10,9,20,null,null,15,7]
        Output: 42
        Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
        """
        solution = Solution()
        tree = TreeNode(-10)
        tree.left = TreeNode(9)
        tree.right = TreeNode(20)
        tree.right.left = TreeNode(15)
        tree.right.right = TreeNode(7)
        output = solution.maxPathSum(root=tree)
        self.assertEqual(output, 42)