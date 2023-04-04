def sum_of_list(a_list):
    if len(a_list) == 1:
        return a_list[0]
    else:
        temp_list = a_list[:]
        temp_list.pop()

    return a_list[len(a_list) - 1] + sum_of_list(temp_list)

list_test = [1,2,3,5]
print(sum_of_list(list_test))