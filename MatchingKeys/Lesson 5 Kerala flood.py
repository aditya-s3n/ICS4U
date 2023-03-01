import csv

def create_kerala_districts(filename):
    
    kerala_flood_info = {}

    with open(filename, "r") as file_in:
        file_in.readline()
        file_in = csv.reader(file_in)

        for area in file_in:
            district = area[0]
            fatalilities = area[1]
            num_of_camps = area[2]
            rainfall_mm = area[3]
            normal_rainfall_mm = area[4]
            num_landslides = area[5]
            full_damaged_houses = area[6]
            
            kerala_flood_info[district] = {
                "fatalilities": fatalilities,
                "num_camps": num_of_camps,
                "actual_rainfall_mm": rainfall_mm,
                "normal_rainfall_mm": normal_rainfall_mm,
                "no_landslides": num_landslides,
                "num_damaged_houses": full_damaged_houses,
                "warnings": []
            }

    return kerala_flood_info
        


def add_kerala_flood_warnings(filename, kerala_flood_info):

    with open(filename, "r") as file_in:
        file_in.readline()
        file_in = csv.reader(file_in)

        for alert in file_in:
            district_name = alert[0]
            alert_info = alert[1:]

            kerala_flood_info[district_name]["warnings"].append(alert_info)




def print_kerala_flood_info(kerala_flood_info):
    for key in (kerala_flood_info):
        print(key)
        print(kerala_flood_info[key])


def main():
    

      flood_dict = create_kerala_districts("district_wise_details.csv")
      add_kerala_flood_warnings("warnings_actual_predicted.csv", flood_dict)

      print_kerala_flood_info(flood_dict)

main()
        
