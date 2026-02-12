import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_74_sum_root_to_leaf_numbes import Solution, TreeNode


class SumRootToLeafNumbersTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Input: root = [1,2,3]
        Output: 25
        Explanation:
        The root-to-leaf path 1->2 represents the number 12.
        The root-to-leaf path 1->3 represents the number 13.
        Therefore, sum = 12 + 13 = 25.
        """
        solution = Solution()
        tree = TreeNode(1, TreeNode(2), TreeNode(3))
        output = solution.sumNumbers(root=tree)
        self.assertEqual(output, 25)

    def test_example_2(self):
        """
        Input: root = [4,9,0,5,1]
        Output: 1026
        Explanation:
        The root-to-leaf path 4->9->5 represents the number 495.
        The root-to-leaf path 4->9->1 represents the number 491.
        The root-to-leaf path 4->0 represents the number 40.
        Therefore, sum = 495 + 491 + 40 = 1026.
        """
        solution = Solution()
        tree = TreeNode(4)
        tree.left = TreeNode(9)
        tree.right = TreeNode(0)
        tree.left.left = TreeNode(5)
        tree.left.right = TreeNode(1)
        output = solution.sumNumbers(root=tree)
        self.assertEqual(output, 1026)