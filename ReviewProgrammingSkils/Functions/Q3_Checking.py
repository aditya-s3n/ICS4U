def isDigit_Int(number: str) -> bool:
    all_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in number:
        if i not in all_nums:
            return False
        
    return True


def isFloat(number: str) -> bool:
    all_nums_float = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    single_decimal_check = False

    for i in number:
        if i not in all_nums_float:
            if i == '.' and not single_decimal_check:
                single_decimal_check = True
            else:
                return False
            
    return True
        
print(isDigit_Int(input("Enter Digit: ")))
print(isFloat(input("Enter Float: ")))
