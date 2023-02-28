import csv

kickstater_dict = {}
kickstater_category_data_dict = {}
with open("ks-projects-201801.csv", encoding="utf-8") as file_kickstarter:

    kickstarter_pointer = csv.DictReader(file_kickstarter)

    for product in kickstarter_pointer:
        if product["category"] not in kickstater_dict:
            kickstater_dict[product["category"]] = []
            
            kickstater_category_data_dict[product["category"]] = {
                "success": 0,
                "failed": 0,
                "cancelled": 0,
                "total": 0
            }


        product_organzied = [
            product["state"], 
            product["country"], 
            product["currency"], 
            product["name"],
            product["deadline"][:10],
            product["goal"],
            product["pledged"],
            product["backers"]
        ]

        kickstater_dict[product["category"]].append(product_organzied)

        
        if product["state"] == "successful":
            kickstater_category_data_dict[product["category"]]["success"] += 1
        elif product["state"] == "failed":
            kickstater_category_data_dict[product["category"]]["failed"] += 1
        elif product["state"] == "canceled":
            kickstater_category_data_dict[product["category"]]["cancelled"] += 1

        kickstater_category_data_dict[product["category"]]["total"] += 1



for category, value in kickstater_category_data_dict.items():
    success_rate = (value["success"] / value["total"]) * 100
    failed_rate = (value["failed"] / value["total"]) * 100
    cancelled_rate = (value["cancelled"] / value["total"]) * 100

    print(f"""\
    {category}:
        Success: {success_rate:.2f}%
        Failure: {failed_rate:.2f}%
        Cancelled: {cancelled_rate:.2f}%
    """)

    