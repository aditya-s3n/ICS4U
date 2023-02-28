import csv

ramen_organized_dict = {}
with open("ramen-ratings.csv", encoding="utf-8") as file_ramen:

    ramen_dict = csv.DictReader(file_ramen)

    for ramen in ramen_dict:
        if ramen["Country"] not in ramen_organized_dict:
            ramen_organized_dict[ramen["Country"]] = {}

        if ramen["Style"] not in ramen_organized_dict[ramen["Country"]]:
            ramen_organized_dict[ramen["Country"]][ramen["Style"]] = []

        ramen_organized_dict[ramen["Country"]][ramen["Style"]].append([ramen["Brand"], ramen["Variety"], ramen["Stars"]])

print(ramen_organized_dict)