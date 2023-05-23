import turtle
import math


class Sun:
   def __init__(self, iname, irad, im, itemp):
      self._name = iname
      self._radius = irad
      self._mass = im
      self._temp = itemp
      self._x = 0
      self._y = 0

      self.sturtle = turtle.Turtle()
      self.sturtle.shape("circle")
      self.sturtle.color("yellow")

   def name(self):
      return self._name

   def radius(self):
      return self._radius

   def mass(self):
      return self._mass

   def temperature(self):
      return self._temp

   def volume(self):
      v = 4.0/3 * math.pi * self._radius**3
      return v

   def surface_area(self):
      sa = 4.0 * math.pi * self._radius**2
      return sa

   def density(self):
      d = self._mass / self.volume()
      return d

   def set_name(self, newname):
      self._name = newname

   def set_radius(self, r):
      self._radius = r

   def __str__(self):
      return self._name

   def getXPos(self):
      return self._x

   def getYPos(self):
      return self._y


class Planet:

   def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
      self._name = iname
      self._radius = irad
      self._mass = im
      self._distance = idist
      self._x = idist
      self._y = 0

      self._velx = ivx
      self._vely = ivy
      self._colour = ic
      self._num_moons = 0
      self._moon_list = []

      self.pturtle = turtle.Turtle()
      self.pturtle.up()
      self.pturtle.color(self._colour)
      self.pturtle.shape("circle")
      self.pturtle.goto(self._x,self._y)
      self.pturtle.down()
      self.pturtle.shapesize(irad * 0.015, irad * 0.015)

   def get_num_moons(self):
      return self._num_moons

   def change_size(self, new_size):
      self._radius = new_size
      self.pturtle.shapesize(new_size, new_size)
      
   def name(self):
      return self._name

   def radius(self):
      return self._radius

   def mass(self):
      return self._mass

   def distance(self):
      return self._distance

   def volume(self):
      v = 4.0/3 * math.pi * self._radius**3
      return v

   def surfaceArea(self):
      sa = 4.0 * math.pi * self._radius**2
      return sa

   def density(self):
      d = self._mass / self.get_volume()
      return d

   def circumference(self):
      c = 2.0 * math.pi * self._radius ** 2
      return c

   def set_name(self, newname):
      self._name = newname  

   def __str__(self):
      return f'{self._name:<12} {self._colour} on screen'
   
   def __repr__(self):
      return self._name
   
   def __lt__(self, other):
      return self._distance < other.distance()
   
   def __gt__(self, other):
      return self._distance > other.distance()
   
   def __eq__(self, other):
      return self._distance == other.distance()

   def move_to(self, newx, newy):
      self._x = newx
      self._y = newy
      self.pturtle.goto(newx, newy)

   def getXPos(self):
      return self._x

   def getYPos(self):
      return self._y

   def getXVel(self):
      return self._velx

   def getYVel(self):
      return self._vely

   def setXVel(self, newvx):
      self._velx = newvx

   def setYVel(self, newvy):
      self._vely = newvy

   def set_moons(self, n):
      self._num_moons = n

   def add_moon(self, new_moon):
      self._moon_list.append(new_moon)


class SolarSystem:
   def __init__(self, width, height):
      self._thesun = None
      self._planets = []
      self.ssturtle = turtle.Turtle()
      self.ssturtle.hideturtle()
      self.ssscreen = turtle.Screen()
      self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0)
      self.ssscreen.tracer(50)

   def add_planet(self, aplanet):
      self._planets.append(aplanet)

   def total_mass(self):
      mass = 0
      for planet in self._planets:
         mass += planet.mass()

      return mass + self._thesun.mass()
   
   def remove_planet(self, aplanet):
      self._planets.remove(aplanet)

   def sort_planets(self):
      self._planets.sort()

   def __str__(self):
      return f"Sun: {self._thesun}\
               Planets: {self._planets}"
      
   def __len__(self):
      return len(self._planets)

   def add_sun(self, sun):
      self._thesun = sun

   def freeze(self):
      self.ssscreen.exitonclick()

   def move_planets(self):
      G = 0.1
      dt = 0.001

      for p in self._planets:   
         p.move_to(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

         rx = self._thesun.getXPos() - p.getXPos()
         ry = self._thesun.getYPos() - p.getYPos()
         r = math.sqrt(rx**2 + ry**2)

         accx = G * self._thesun.mass()*rx/r**3
         accy = G * self._thesun.mass()*ry/r**3

         p.setXVel(p.getXVel() + dt * accx)

         p.setYVel(p.getYVel() + dt * accy)



def createSSandAnimate():
   ss = SolarSystem(3, 3)
   
   sun = Sun("SUN", 5000, 10, 5800)
   ss.add_sun(sun)

   earth = Planet("EARTH", 47.5, 5000, 0.3, 0, 1.0, "green")
   ss.add_planet(earth)

   mars = Planet("MARS", 50, 9000, 0.5, 0, 1.63, "red")
   ss.add_planet(mars)

   mercury = Planet("MERCURY", 19.5, 1000, .25, 0, 2, "blue")
   ss.add_planet(mercury)

   jupiter = Planet("JUPITER", 100, 49000, 0.7, 0, 2, "black")
   ss.add_planet(jupiter)

   saturn = Planet("Saturn", 58, 14700, 1.4, 0, 2, "purple")
   ss.add_planet(saturn)

   print(f"Lenght of the solar system: {len(ss)}")
   print(f"Total mass of the solar system: {ss.total_mass()}")
   print(f"Breakdown of masses:\
         {sun.mass()}\
         {earth.mass()}\
         {mars.mass()}\
         {mercury.mass()}\
         {jupiter.mass()}")
   
   print(ss)
   ss.sort_planets()
   print(ss)

   num_time_periods = 100000
   for amove in range(num_time_periods):
      ss.move_planets()

   ss.freeze()       


   
      
createSSandAnimate()

