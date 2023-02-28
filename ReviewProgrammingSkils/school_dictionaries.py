def create_school_dictionary(school_codes, school_names):
    school_dictionairy = {}

    for i in range(len(school_codes)):
        school_dictionairy[school_codes[i]] = school_names[i]

    return school_dictionairy

print(create_school_dictionary(['aph', 'irs'], ['Abbey Park', 'Iroquois Ridge']))