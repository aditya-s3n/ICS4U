hexcode_dict = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

class Colour:

    def __init__(self, r, g, b):

        self._red = r
        self._green = g
        self._blue = b


    def red(self):
        return self._red
    
    def green(self):
        return self._green
    
    def blue(self):
        return self._blue
    
    def __str__(self):
        return f"({self._red}, {self._green}, {self._blue})"
    
    def __repr__(self):
        return f"({self._red}, {self._green}, {self._blue})"

    def __add__(self, other):
        red = self._red + other.red()
        green = self._green + other.green()
        blue = self._blue + other.blue()

        newColor = Colour(red, green, blue)

        return newColor


    def __sub__(self, other):
        red = self._red - other.red()
        green = self._green - other.green()
        blue = self._blue - other.blue()

        newColor = Colour(red, green, blue)
        
        return newColor

    def __eq__(self, other):
        red_bool = self._red == other.red()
        green_bool = self._green == other.green()
        blue_bool = self._blue == other.blue()

        return red_bool and green_bool and blue_bool

    
    def hex(self):
        redInitial = self._red // 16
        redSecondary = (self._red / 16) % 1

        greenInitial = self._green // 16
        greenSecondary = (self._green / 16) % 1

        blueInitial = self._blue // 16
        blueSecondary = (self._blue / 16) % 1

        return f'#{hexcode_dict[redInitial]}{hexcode_dict[redSecondary]}{hexcode_dict[greenInitial]}{hexcode_dict[greenSecondary]}{hexcode_dict[blueInitial]}{hexcode_dict[blueSecondary]}'


    def luminosity(self):
        rgb = [self._red, self._green, self._blue]

        luminosity_formula = 0.5 * ((max(rgb) / 255) + (min(rgb) / 255))

        return luminosity_formula

    def saturation(self):
        rgb = [self._red, self._green, self._blue]
        luminosity = self.luminosity()

        if max(rgb) == min(rgb):
            saturation =  0
        elif luminosity <= 0.5:
            saturation = ((max(rgb) / 255) - (min(rgb) / 255)) / luminosity
        else :
            saturation = ((max(rgb) / 255) - (min(rgb) / 255)) / (2 - (max(rgb) / 255) - (min(rgb) / 255))

        return saturation
    
    def __lt__(self, other):
        return self.saturation() < other.saturation()
    
    def __gt__(self, other):
        return self.saturation() > other.saturation()
    
    def __le__(self, other):
        return self.saturation() <= other.saturation()
    
    def __ge__(self, other):
        return self.saturation() >= other.saturation()
    
    
