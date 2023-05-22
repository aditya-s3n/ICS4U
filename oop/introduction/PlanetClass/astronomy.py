import math

class Planet:
  

    def __init__(self, name, t, orbit, num_moons, radius, moon_list = []):
        self._name = name
        self._type = t
        self._orbit_days = orbit
        self._num_moons = num_moons
        self._moon_list = moon_list
        self._radius = radius


    def name(self):
        return self._name

    def change_type(self, new):
        self._type = new

    def orbit_day(self):
        return self._orbit_days
    
    def num_moons(self):
        return self._num_moons

    def change_orbit_day(self, new):
        self._orbit_days = new

    def change_num_moonds(self, new_moons):
        self._num_moons = new_moons

    def add_moon(self, new_moon):
        self._moon_list.append(new_moon)

    def get_circumference(self):
        return (2 * self._radius) * math.pi
    
