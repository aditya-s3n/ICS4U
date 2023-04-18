def get_last_name(student):
    return student["last_name"]
    
def main():
    
    student = {"name": "Sam Blainey", "courses": "ICS4U, MCV4U, SBIO4U"}

    try:
        name = get_last_name(student)
        print("All exceptions caught! Good job!")
        print(f'The student\'s last name is {name}')
    
    except KeyError:
        print(f"Key Error\
              Key Inputed: last_name\
              Dictionary: {student}")

main()