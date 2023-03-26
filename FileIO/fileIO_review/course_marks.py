marksDict = {}


with open("courseMarks.txt", "r") as file_marks:

    for line in file_marks:
        line = line.strip().split(",")

        student = line[0]
        course = line[1]
        mark = line[2]

        if course not in marksDict:
            marksDict[course] = {}

        marksDict[course][student] = int(mark)

print(marksDict)