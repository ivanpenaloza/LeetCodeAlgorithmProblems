import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_63_rotate_linked_list import Solution, ListNode

class RotateLinkListTestCase(unittest.TestCase):

    def create_linked_list(self, values):
        """
        Helper function to create a linked list from a list of values.
        
        :param values: List of node values
        :return: Head of the linked list
        """
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head

    def linked_list_to_list(self, head):
        """
        Helper function to convert linked list to Python list.
        
        :param head: Head of the linked list
        :return: List of values
        """
        result = []
        current = head
        
        while current:
            result.append(current.val)
            current = current.next
        
        return result

    def test_first_pattern(self):
        # Example 1: Input: head = [1,2,3,4,5], k = 2
        # Output: [4,5,1,2,3]
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        output = solution.rotateRight(head, 2)
        result = self.linked_list_to_list(output)
        target = [4, 5, 1, 2, 3]
        self.assertEqual(result, target)

    def test_second_pattern(self):
        # Example 2: Input: head = [0,1,2], k = 4
        # Output: [2,0,1]
        solution = Solution()
        head = self.create_linked_list([0, 1, 2])
        output = solution.rotateRight(head, 4)
        result = self.linked_list_to_list(output)
        target = [2, 0, 1]
        self.assertEqual(result, target)