def spread_counting_sort(minimum, maximum, a_list):
    spread = maximum - minimum
    offset_value = minimum

    counting_list = [0] * spread

    for element in range(0, len(a_list)):
        index = element - offset_value
        counting_list[index] = counting_list[index] + 1

    

