import unittest

import reverse_character

class reverse_character_test(unittest.TestCase):

    def test_that_index_of_character_in_a_word_is_returned(self):
    
        word = "abcdefgh"
        
        char = 'd'
        
        actual = reverse_character.get_char_index(word,char)
        
        self.assertEqual(3, actual)
    
    def test_that_minus_one_is_returned_when_character_is_not_found(self):

        word = "hello"
        char = "x"

        actual = reverse_character.get_char_index(word, char)

        self.assertEqual(-1, actual)
        
    def test_that_word_is_reversed_from_a_given_index(self):
        
        word = "abcdefgh"
        
        char = 'd'
        
        actual = reverse_character.reverse_from_character_index(word, char)
        
        self.assertEqual("dcbahgfe", actual)
        
    def test_that_same_word_is_returned_when_character_is_not_found_in_word(self):
    
        word = "abcdefgh"
        
        char = 'j'
        
        actual = reverse_character.reverse_from_character_index(word, char)
        
        self.assertEqual("abcdefgh", actual)
