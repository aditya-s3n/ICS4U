import math

class Sun:
    def __init__(self, name, radius, mass, temperature):
        self._name = name
        self._radius = radius
        self._mass = mass
        self._temperature = temperature

    def name(self):
        return self._name
    
    def radius(self):
        return self._radius
    
    def temperature(self):
        return self._temperature
    
    def volume(self):
        return ((4/3) * math.pi * (self._radius ** 3))
    
    def surface_area(self):
        return (4 * math.pi * (self._radius ** 2))
    
    def change_name(self, name):
        self._name = name

    def change_radius(self, radius):
        self._radius = radius