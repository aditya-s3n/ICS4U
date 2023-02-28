def rot_13_encryption(phrase, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    phrase = phrase.lower()

    encrypted_phrase = ""
    for letter in phrase:
        index_of_letter = alphabet.find(letter)
        
        index_of_letter += shift

        while index_of_letter > 25:
            index_of_letter -= 25

        encrypted_phrase += alphabet[index_of_letter]

    return encrypted_phrase

word = input("Word to encrypt: ")
shift = int(input("Shift Value: "))
print(rot_13_encryption(word, shift))
            