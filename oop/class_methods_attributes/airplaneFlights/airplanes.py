class Aircraft:

    def __init__(self):
        pass

    def num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)

class SmallPretendPlane(Aircraft):

    def model(self):
        return 'Small Pretend Plane'

    def seating_plan(self):
        return range(1, 4), "AB"
    

class AirbusA319(Aircraft):
    
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEFGHJK"

