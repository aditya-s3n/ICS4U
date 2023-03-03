import requests
import random
import csv

#get data from api
def getRandomPerson():
    response = requests.get("https://random-data-api.com/api/v2/users")
    response = response.json()


    randomID = getRandomID()
    random_salary = getRandomSalary()
    random_name = response["first_name"] + " " + response["last_name"]
    random_job = response["employment"]["title"]

    return [randomID, random_name, random_job, random_salary]
    

def getRandomID():
    randomID = list(str(random.randint(100000000, 999999999)))
    randomID.insert(3, "-")
    randomID.insert(6, "-")

    return "".join(randomID)

def getRandomSalary():
    random_salary = list(str(random.randint(25000, 125000)))

    random_salary.insert(0, "$")
    random_salary.insert(-3, " ")

    return "".join(random_salary)




with open("random_data.csv", "w", newline="") as random_data_file:
    writer = csv.writer(random_data_file)
    
    for i in range(500):
        random_person = getRandomPerson()

        writer.writerow(random_person)