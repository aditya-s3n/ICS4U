import random

def even_odd_list(number_values, low_value, high_value):
    even_list = []
    odd_list = []

    while len(even_list) + len(odd_list) < number_values:
        random_number = random.randint(low_value, high_value)

        if random_number % 2 == 0 and len(even_list) * 2 < number_values and random_number not in even_list:
            even_list.append(random_number)
        elif random_number % 2 != 0 and len(odd_list) * 2 < number_values and random_number not in odd_list:
            odd_list.append(random_number)

    return even_list + odd_list

print(even_odd_list(100, 10, 20000))
