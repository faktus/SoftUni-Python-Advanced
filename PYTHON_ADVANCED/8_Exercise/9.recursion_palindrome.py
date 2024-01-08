def palindrome(word, index):
    word_list = list(word)
    
    if -len(word) == index:
        return ''
    index -= 1
    return word_list[index] + palindrome(word, index)

    

print(palindrome("peter", 0))