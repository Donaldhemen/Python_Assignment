import unittest

import Solution
class TestMergeSortedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sorted_list(self):
        self.assertEqual(self.solution.sortList(self.solution.sortList()))

    def test_merge_sorted_list(self):
        self.assertEqual(self.solution.mergeTwoLists([1,3,2], [1,4,2]), [1,1,2,2,3,4])
