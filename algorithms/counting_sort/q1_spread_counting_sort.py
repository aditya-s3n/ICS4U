def spread_counting_sort(minimum, maximum, a_list):
    spread = maximum - minimum
    offset_value = minimum

    counting_list = [0] * (spread + 1)

    for element in range(0, len(a_list)):
        index = a_list[element] - offset_value
        counting_list[index] = counting_list[index] + 1

    a_list.clear()
    for i in range(0, len(counting_list)):
        element = counting_list[i]

        while element != 0:
            value = i + offset_value
            a_list.append(value)
            
            element -= 1


numbers = [-1, -4, 0, 11, 33, 33, 11212, 33]
spread_counting_sort(-4, 11212, numbers)
print(numbers)