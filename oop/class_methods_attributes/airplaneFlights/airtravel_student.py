import airplanes

class Flight:

    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = Flight._generate_seating_plan(rows, seats)
        
    #generate a dictionary for each row to hold
    #passenger booking information
    @classmethod
    def _generate_seating_plan(cls, rows, seats):
        seat_dict = {}

        for letter in seats:
            seat_dict[letter] = None

        seating_plan = []

        for row in rows:
            seating_plan.append(seat_dict)

        return seating_plan

       
    @classmethod
    def _check_seat(cls, seat):
        row = int(seat[:2])
        seat_num = seat[-1]

        return row, seat_num
        

    def allocate_seat(self, seat, passenger):

        row, letter = Flight._check_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')

        self._seating[row][letter] = passenger
        
        
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft(self):
        return self._aircraft.model()

    def num_seats(self):
        return self._aircraft.num_seats()

    #should be an internal function, not available to applications
    def seating(self):
        return self._seating
       

def make_flights():


    test_plane = airplanes.SmallPretendPlane()
    print(test_plane.seating_plan())

    test_flight = Flight('QQ234', airplanes.SmallPretendPlane())
    print(test_flight.num_seats())
    print(test_flight.seating())
    
    a = airplanes.AirbusA319()
    print(a.model())
    print(a.num_seats())
    print(a.seating_plan())

    b = airplanes.Boeing777()
    print(b.model())
    print(b.num_seats())
    print(b.seating_plan())

    f1 = Flight('BA758', airplanes.AirbusA319())
    f2 = Flight('KL613', airplanes.Boeing777())

    print(f'FlightNo: {f1.number()}\nAirline: {f1.airline()}')
    print(f'Aircraft: {f1.aircraft()}')
    f1.allocate_seat('15C', 'Jayson Harmen')

    print(f1.num_seats(), 'seats on flight')
    print('Seat allocations\n', f1.seating())

    
make_flights()
