def is_palindrome(phrase):
    reversed_phrase = phrase[::-1]
    
    if reversed_phrase == phrase:
        return True
    else:
        return False

print(is_palindrome(input("Enter Phrase: ")))