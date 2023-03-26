def insertion_sort(a_list):
    for element_index in range(1, len(a_list)):

        for compared_element_index in range(element_index - 1, -1, -1):
            orginal_element = a_list[element_index]
            compared_element = a_list[compared_element_index]
            
            if orginal_element >= compared_element:
                a_list.pop(element_index)
                a_list.insert(compared_element_index + 1, orginal_element)
                break

            elif compared_element_index == 0:
                a_list.remove(orginal_element)
                a_list.insert(0, orginal_element)

numbers = [29,10,14,37,14,690,12,123,333,129102,1]
insertion_sort(numbers)
print(numbers)