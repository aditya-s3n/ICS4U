def index_list(some_list, item):
    if some_list[0] == item:
        return 0
    
    return 1 + index_list(some_list[1:], item)

list_test = [0, 3, 4, 5, 32]
print(index_list(list_test, 32))