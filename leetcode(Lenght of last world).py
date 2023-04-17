def lengthOfLastWord(s):
    words = s.split()
    last_word = words[-1]
    len_last_word = len(last_word)
    return f'The last word is "{last_word}" with length {len_last_word}.'
    
print(lengthOfLastWord("Hello Wolrd! QWERTYAFNAJF K:LAGF"))


