import unittest

from class_tasks.perfect_square import is_perfect_square

class PerfectSquareTest(unittest.TestCase):
    
    def test_that_a_perfect_square_in_a_list_returns_true_in_the_list(self):

        self.assertEqual(is_perfect_square([4,9,25,49]), [True,True,True,True])
        
    def test_that_a_number_that_is_not_a_perfect_square_will_return_false_in_the_list(self):
        
        self.assertEqual(is_perfect_square([8,36,49,5]), [False,True,True,False])
