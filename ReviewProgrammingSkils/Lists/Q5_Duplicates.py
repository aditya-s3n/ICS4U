def has_duplicates(list_to_check):
    for i in range(0, len(list_to_check)):
        temp_list = list_to_check
        value_to_check = temp_list[i]
        temp_list[i] = ""

        if value_to_check in list_to_check:
            return True
        
    return False

print(has_duplicates(["Hi", "Hi", "Try"]))