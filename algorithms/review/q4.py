def delete_item_from_list(item, a_list):
    index = 0

    while a_list[index] != item:
        index += 1

    a_list =  a_list[0: index] + a_list[index + 1: len(a_list)]


list_text = [0, 2, 3, 41, 22]
delete_item_from_list(41, list_text)
print(list_text)

# given a list and item in list
# repeat until list[index] = item:
#    index + 1
# list <- list[0:index-1] + list[index+1:n]