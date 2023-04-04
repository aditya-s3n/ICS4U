def flatten_list(list_to_flat):
    if list_to_flat == []:
        return list_to_flat
    
    if type(list_to_flat[0]) == list:
        return flatten_list(list_to_flat[0]) + flatten_list(list_to_flat[1:])
    
    return [list_to_flat[0]] + flatten_list(list_to_flat[1:])
        

print(flatten_list([1, 2, 3, [[0,7], 9, 8], 5, 6]))       #should return 1 2 3 0 7 9 8 5 6
print(flatten_list([1, 2, 3, [[0, 7], 9, [8, 8]], 5, 6])) #should return 1 2 3 0 7 9 8 8 5 6