import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_76_binary_search_tree_iterator import BSTIterator, TreeNode


class BSTIteratorTestCase(unittest.TestCase):

    def test_example_1(self):
        """
        Input: ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
               [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
        Output: [null, 3, 7, true, 9, true, 15, true, 20, false]
        
        Explanation:
        BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
        bSTIterator.next();    // return 3
        bSTIterator.next();    // return 7
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 9
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 15
        bSTIterator.hasNext(); // return True
        bSTIterator.next();    // return 20
        bSTIterator.hasNext(); // return False
        """
        # Build tree: [7, 3, 15, null, null, 9, 20]
        #       7
        #      / \
        #     3   15
        #        /  \
        #       9    20
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)
        
        bst_iterator = BSTIterator(root)
        
        self.assertEqual(bst_iterator.next(), 3)
        self.assertEqual(bst_iterator.next(), 7)
        self.assertTrue(bst_iterator.hasNext())
        self.assertEqual(bst_iterator.next(), 9)
        self.assertTrue(bst_iterator.hasNext())
        self.assertEqual(bst_iterator.next(), 15)
        self.assertTrue(bst_iterator.hasNext())
        self.assertEqual(bst_iterator.next(), 20)
        self.assertFalse(bst_iterator.hasNext())