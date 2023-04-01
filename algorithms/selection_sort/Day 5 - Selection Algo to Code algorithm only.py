

#OUT OF PLACE SORT

def selection_sort(a_list):
    unsorted_list = a_list[:]
    a_list.clear()

    for i in range(0, len(unsorted_list)):
        minimum = unsorted_list[i]

        for next_element in range(i + 1, len(unsorted_list)):
            compared_element = unsorted_list[next_element]

            if compared_element < minimum:
                minimum = compared_element

        unsorted_list.remove(minimum)
        unsorted_list.insert(i, minimum)
        a_list.append(minimum)
        
        
    

numbers = [8, 8, 18, 13, 36, 0, 2, -2, -5]
selection_sort(numbers)
print(numbers)



#IN PLACE SORT
#Algorithm provided by visualgo.net

def selection_sort(a_list):
    
    for i in range(0, len(a_list) - 1):
        minimum = a_list[i]
        index_minimum = i

        for next_index in range(i, len(a_list)):
            compared_element = a_list[next_index]

            if compared_element < minimum:
                index_minimum = next_index
                minimum = compared_element

        a_list.pop(index_minimum)
        a_list.insert(i, minimum)

numbers = [8, 8, 18, 13, 36, 0, 2, -2, -5]
selection_sort(numbers)
print(numbers)





    
