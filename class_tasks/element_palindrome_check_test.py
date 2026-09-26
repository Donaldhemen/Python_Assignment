import unittest

import element_palindrome_check

class element_palindrome_check_test(unittest.TestCase):

    def test_that_a_word_is_reversed(self):
        
        word = "hello"
        
        actual = element_palindrome_check.reverse_word(word)
        
        self.assertEqual("olleh", actual)
        
    def test_that_a_word_is_a_palindrome(self):
        
        word = "Madam"
        
        actual = element_palindrome_check.is_palindrome(word)
        
        self.assertEqual(True, actual)
        
    def test_that_a_word_is_not_a_palindrome(self):
    
        word = "hello"
        
        actual = element_palindrome_check.is_palindrome(word)
        
        self.assertEqual(False, actual)
    
    def test_that_a_palindrome_word_in_a_list_returns_true_in_the_list(self):
        
        words = ["Madam", "noon", "racecar"]
        
        actual = element_palindrome_check.is_palindrome_element(words)
        
        self.assertEqual([True,True,True], actual)
