import random

def createTestValues(upper_range, amount):
    '''
    Function returns a list of randomly generated numbers

    Params:
    upper_range is highest random value to be included in list
    amount is the number of values to include in the list

    Returns:
    aList The generated list of random values
    '''
    aList = []
    for i in range(amount):
        aList.append(random.randint(0, upper_range))

    return aList
    

def countingSort(aList):
    '''Function returns a list of values sorted in ascending order.

    Params:
    aList is the list to be sorted

    Return sortedList is the new sorted list
    '''

    #create the key or counting array based on max value in list
    key = []
    for i in range(0, max(aList) + 1):
        key.append(0)

    
    #iterate through given list and increase counters of key
    #for each element in list
    for num in aList:
        #increase the respective counter by 1
        key[num] += 1

    #create a new list with values in sorted order based on couters of key
    sorted_list = []
    #for each counter, starting from smallest key
    for i in range(0, len(key)):
        counter = key[i]
        
        #while counter is non-zero
        while(counter > 0):
            #restore element to list
            sorted_list.append(i)
            #decrease counter by 1
            counter -= 1

        

    return sorted_list

        
#main
def main():
    
    list_of_numbers = createTestValues(50, 1000)
    list_of_numbers = countingSort(list_of_numbers)

    print(list_of_numbers)

main()
