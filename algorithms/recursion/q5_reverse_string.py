def reverse_string(phrase):
    if len(phrase) == 1:
        return phrase
    
    return phrase[-1] + reverse_string(phrase[:-1])

print(reverse_string('hello world'))