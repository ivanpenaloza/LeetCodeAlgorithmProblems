import unittest
from typing import Optional, List
from src.my_project.interviews.top_150_questions_round_22\
.ex_71_populating_next_right_pointer_in_each_node import Solution, Node

class PopulatingNextRightPointersInEachNodeTestCase(unittest.TestCase):

    def build_tree(self, values: List[Optional[int]]) -> Optional[Node]:
        """Build tree from level-order list representation."""
        if not values:
            return None
        
        root = Node(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Add left child
            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1
            
            # Add right child
            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1
        
        return root

    def verify_next_pointers(self, root: Optional[Node]) -> List[str]:
        """Verify next pointers and return serialized output."""
        if not root:
            return []
        
        result = []
        leftmost = root
        
        while leftmost:
            current = leftmost
            while current:
                result.append(str(current.val))
                current = current.next
            result.append('#')
            
            # Move to next level
            leftmost = leftmost.left if leftmost.left else leftmost.right
            if not leftmost:
                # Find the first node in the next level
                temp = root
                queue = [root]
                while queue:
                    node = queue.pop(0)
                    if node.left and node.left not in [n for level in [root] for n in [root]]:
                        leftmost = node.left
                        break
                    if node.right:
                        leftmost = node.right
                        break
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                break
        
        return result

    def get_level_order_with_next(self, root: Optional[Node]) -> str:
        """Get level order traversal following next pointers."""
        if not root:
            return ""
        
        result = []
        leftmost = root
        
        while leftmost:
            current = leftmost
            level_vals = []
            while current:
                level_vals.append(str(current.val))
                current = current.next
            result.extend(level_vals)
            result.append('#')
            
            # Find leftmost node of next level
            temp = leftmost
            leftmost = None
            while temp and not leftmost:
                if temp.left:
                    leftmost = temp.left
                elif temp.right:
                    leftmost = temp.right
                else:
                    temp = temp.next
        
        return ','.join(result)

    def test_example_1(self):
        """
        Input: root = [1,2,3,4,5,null,7]
        Output: [1,#,2,3,#,4,5,7,#]
        """
        solution = Solution()
        root = self.build_tree([1, 2, 3, 4, 5, None, 7])
        result = solution.connect(root)
        output = self.get_level_order_with_next(result)
        expected = "1,#,2,3,#,4,5,7,#"
        self.assertEqual(output, expected)

    def test_example_2(self):
        """
        Input: root = []
        Output: []
        """
        solution = Solution()
        root = self.build_tree([])
        result = solution.connect(root)
        output = self.get_level_order_with_next(result)
        expected = ""
        self.assertEqual(output, expected)