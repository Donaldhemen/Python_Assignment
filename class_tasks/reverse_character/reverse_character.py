
def get_char_index(word, target_char):
    
    index = 0
    
    while index < len(word):
        
        if word[index] == target_char:
        
            return index
            
        index += 1
            
    return -1

def reverse_from_character_index(word, target_char):
    
    if target_char not in word:
    
        return word
    
    index = get_char_index(word, target_char)
    
    first_part = word[index::-1] 
    
    second_part = word[-1:index:-1]
    
    return first_part + second_part


