university_programs_dict = {}

with open("university_programs.txt") as university_file:
    for line in university_file:
        line = line.split(":")

        universities = line[0].strip().split(",  ")
        programs = line[1].split(",")


        for program in programs:
            program = program.strip()

            if program not in university_programs_dict:
                university_programs_dict[program] = universities
            else:
                old_list = university_programs_dict[program]
                added_list = list(dict.fromkeys(old_list + universities))

                university_programs_dict[program] = added_list

print(university_programs_dict["Electrical Engineering"])
