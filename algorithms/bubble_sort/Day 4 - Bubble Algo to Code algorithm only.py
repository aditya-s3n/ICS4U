
def bubble_sort(a_list):
    swapped = True

    while swapped:
        swapped = False

        for i in range(0, len(a_list) - 1):
            left_element = a_list[i]
            right_element = a_list[i + 1]

            if left_element > right_element:
                a_list[i] = right_element
                a_list[i + 1] = left_element

                swapped = True


a = [5, 4, 6, 2, 4, 6, 7, 8, 1]
bubble_sort(a)
print(a)
