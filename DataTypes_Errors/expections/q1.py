def do_stuff_with_number(n):
    print(n)

def main():
    the_list = [1, 2, 3, 4, 5]

    
    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])

        except IndexError:
            print(f"Index Error\
                    Length List: {len(the_list)}\
                    Index: {i}")
            break

main() 