braille_dictionary = {"xooooo": "a", "xoxooo": "b", "xxoooo": 'c', 'xxoxoo': 'd',
                      'xooxoo': 'e', "xxxooo": 'f', 'xxxxoo': 'g', 'xoxxoo': 'h',
                      'oxxooo': 'i', 'oxxxoo': 'j', 'xoooxo': 'k', 'xoxoxo': 'l',
                      'xxooxo': 'm', 'xxoxxo': 'n', 'xooxxo': 'o', 'xxxoxo': 'p',
                      'xxxxxo': 'q', 'xoxxxo': 'r', 'oxxoxo': 's', 'oxxxxo': 't',
                      'xoooxx': 'u', 'xoxoxx': 'v', 'oxxxox': 'w', "xxooxx": 'x',
                      'xxoxxx': 'y', "xooxxx": 'z', 'oooooo': ' '}

with open("data22.txt") as braille_file:
    #get all the lines of braille
    message = braille_file.readlines()

    #group my 3, to message lengths
    seperated_message = []
    for i in range(0, len(message), 3):
        seperated_message.append([message[i].strip(), message[i + 1].strip(), message[i + 2].strip()])

    #group by each braille letter
    for row in seperated_message:
        for i in range(0, len(row[0]) - 2, 2):
            braille_character = row[0][i:i+2] + row[1][i:i+2] + row[2][i:i+2]

            print(braille_dictionary[braille_character], end="")
