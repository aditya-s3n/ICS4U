def is_Leap_Year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            
            else:
                return False
        
        else:
            return True
    
    return False

print(is_Leap_Year(int(input('Enter Year: '))))