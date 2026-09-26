    
def reverse_word(word):

    word = word.lower()
    
    reversed_word = word[::-1]
        
    return reversed_word
    
def is_palindrome(word):
    
    return word.lower() == reverse_word(word)

def is_palindrome_element(words):

    words_check = []
    
    for word in words:
    
        if is_palindrome(word):
            words_check.append(True)
            
        else:
            words_check.append(False)
            
    return words_check

