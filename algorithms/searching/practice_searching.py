def insert_item_in_list(element, a_list):
    minimum_value = min(a_list)
    maximum_value = max(a_list)

    if element <= minimum_value:
        a_list.insert(0, element)
    elif element >= maximum_value:
        a_list.insert(len(a_list), element)
    
    else:
        left = 0
        right = len(a_list) - 1
        middle = (left + right) // 2

        left_element = a_list[middle - 1]
        right_element = a_list[middle + 1]
        middle_element = a_list[middle]

        while not(element >= left_element) and not(element <= right_element):
            if element > middle_element:
                right = middle - 1
            elif element < middle_element:
                left = middle + 1

            middle = (left + right) // 2

            left_element = a_list[middle - 1]
            right_element = a_list[middle + 1]
            middle_element = a_list[middle]

        a_list.insert(middle, element)
        
            

# Scenario - value inserted at beginning of list
a = [ 3, 4, 4, 6, 8, 10, 14, 14 ]
insert_item_in_list(1, a)
print(a)
# insert value = 1 into list will produce 
# a = [ 1, 3, 4, 4, 6, 8, 10, 14, 14 ]


# Scenario - value inserted in middle of list
a = [ 3, 4, 4, 6, 8, 10, 14, 14 ]
insert_item_in_list(5, a)
print(a)
# insert value = 5 into list will produce
# a = [ 3, 4, 4, 5, 6, 8, 10, 14, 14 ]
a = [ 3, 4, 4, 6, 8, 10, 14, 14 ]
insert_item_in_list(4, a)
print(a)

a = [ 3, 4, 4, 6, 8, 10, 14, 14 ]
insert_item_in_list(99, a)
print(a)