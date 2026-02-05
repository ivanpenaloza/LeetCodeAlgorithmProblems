import unittest
from src.my_project.interviews.top_150_questions_round_22\
.ex_65_lru_cache import LRUCache

class LRUCacheTestCase(unittest.TestCase):

    def test_example_1(self):
        # Example 1:
        # Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        #        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        # Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
        
        lRUCache = LRUCache(2)
        self.assertIsNone(lRUCache.put(1, 1))  # cache is {1=1}
        self.assertIsNone(lRUCache.put(2, 2))  # cache is {1=1, 2=2}
        self.assertEqual(lRUCache.get(1), 1)    # return 1
        self.assertIsNone(lRUCache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(lRUCache.get(2), -1)   # returns -1 (not found)
        self.assertIsNone(lRUCache.put(4, 4))  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(lRUCache.get(1), -1)   # return -1 (not found)
        self.assertEqual(lRUCache.get(3), 3)    # return 3
        self.assertEqual(lRUCache.get(4), 4)    # return 4