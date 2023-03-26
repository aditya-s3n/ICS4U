
wine_dict = {}

with open("winemag.txt", "r", encoding="utf-8") as file_wine:
    file_wine.readline()

    for line in file_wine:
        line = line.strip().split("\t")

        winery = line[7]
        designation = line[2]
        price = line[4]

        key = f"{winery} | {designation}"
        
        if price != "":
            wine_dict[key] = int(price)

print(wine_dict)
