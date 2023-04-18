def example1():
    for i in range( 3 ):
        try: 
            x = int( input( "enter a number: " ) )
            y = int( input( "enter another number: " ) )
            print( f'{x} / {y} = {x/y}' )

        except ZeroDivisionError:
            print("Tried to divide by Zero!!!")


def example2( L ):
    print( "\n\nExample 2" )
    try:
        sum = 0
        sumOfPairs = []
        for i in range( len( L ) ):
            try:
                sumOfPairs.append( L[i]+L[i+1] )
            except IndexError:
                print(f"Index {i} does not exist\
                      List: {L}\
                      Lenght of List: {len(L)}")

        print( f' sumOfPairs = {sumOfPairs}')

    except TypeError:
        print(f"The list contains non number dataypes\
              List: {L}")


def print_upper_file( filename ):
    try:
        file = open( filename, "r" )
        for line in file:
            print( line.upper() )
        file.close()

    except FileNotFoundError:
        print(f"File {filename} not found in working directory")

    

def main():
    example1()
    
    example2( [ 10, 3, 5, 6, 9, 3 ] )
    example2( [ 10, 3, 5, 6, "NA", 3 ] )
    
    print_upper_file( "doesNotExistYet.txt" )
    print_upper_file( "./Dessssktop/misspelled.txt" )


main()