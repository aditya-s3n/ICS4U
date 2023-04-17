def encode_message(message):
    message = message.strip()
    
    if len(message) > 1:
        message = list(message)
        message[0], message[-1] = message[-1], message[0]

        for i in range(0, len(message), 2):
            message[i], message[i + 1] = message[i + 1], message[i]

        message = "".join(message)

    return message.upper()





#Test Cases
print('\nTest case 1 - empty string')
result = encode_message('')
print(result == '')

print('\nTest case 2 - one character string')
result = encode_message('A')
print(result == 'A')

print('\nTest case 3 - one character + spaces')
result = encode_message('    A     ')
print(result == 'A')

print('\nTest case 4 - 4 characters and no space')
result = encode_message('gold')
print(result == 'ODGL')