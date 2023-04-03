def make_list(file):
    list_out = []

    with open(file) as file_in:
        for line in file_in:
            list_out.append(float(line.strip()))

    return list_out

def counting_sort(a_list):
    money_dict = {}
    for i in range(0, len(a_list)):
        element = a_list[i]

        if element not in money_dict:
            



money_list = make_list("lotsOfMoney.txt")
counting_sort(money_list)

print(money_list)

