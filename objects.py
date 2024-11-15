from decimal import Decimal
import numpy as np

G = Decimal("6.67e-11") #(N * m^2) / kg^2

class OrbitingBody():
    def __init__(self, name, color, aphelion, perihelion, mass):
        self.name = name
        self.color = color
        self.aphelion = Decimal(aphelion)
        self.perihelion = Decimal(perihelion)
        self.mass = Decimal(mass)
        self.semimajor_axis = round(Decimal((self.aphelion + self.perihelion)/2), 10)
        self.focal_distance = round(Decimal(self.aphelion - self.semimajor_axis), 10)
        self.semiminor_axis = round(Decimal(np.sqrt(self.semimajor_axis**2 - self.focal_distance**2)), 10)
        self.eccentricity = round(Decimal(self.focal_distance/self.semimajor_axis), 10)
        self.referenceRadius = round(Decimal(self.semiminor_axis**2 / self.semimajor_axis), 10)
    def printOrbitingValues(self):
        print("Object: " + self.name)
        print(f"Color: {self.color}")
        print(f"Aphelion: {self.aphelion} au")
        print(f"Perihelion: {self.perihelion} au")
        print(f"Semi-major axis: {self.semimajor_axis} au")
        print(f"Focal Distance: {self.focal_distance} au")
        print(f"Semi-minor axis: {self.semiminor_axis} au")
        print(f"Eccentricity: {self.eccentricity}")
        print(f"R_0: {self.referenceRadius}")

class CentralBody():
    def __init__(self, name, color, mass):
        self.name = name
        self.color = color
        self.mass = Decimal(mass) #In Kilograms
    def printCentralBodyValues(self):
        print(f"Central Body: {self.name}")
        print(f"Color: {self.color}")

def KmToAu(aphelion_in_km, perihelion_in_km):
    one_au = Decimal("149597870.7")
    aphelion_in_au = aphelion_in_km / one_au
    perihelion_in_au = perihelion_in_km / one_au
    return round(aphelion_in_au, 10), round(perihelion_in_au, 10)

MERCURY = OrbitingBody("Mercury", "#918b8a", "0.466", "0.307")
VENUS = OrbitingBody("Venus", "#d18e08", "0.728", "0.718")
EARTH = OrbitingBody("Earth", "green", "1.017", "0.983", "5.972e24")
MARS = OrbitingBody("Mars", "#ff0000", "1.665", "1.381")
JUPITER = OrbitingBody("Jupiter", "#c7991c", "5.458", "4.950")
SATURN = OrbitingBody("Saturn", "#a88932", "10.115", "9.048")
URANUS = OrbitingBody("Uranus", "#23ccc6", "20.083", "18.375")
NEPTUNE = OrbitingBody("Neptune", "#234dcc", "30.441", "29.766")
SUN = CentralBody("Sun", "#dbc70d", "1.98e30")
PLANETS = [MERCURY, VENUS, EARTH, MARS, JUPITER, SATURN, URANUS, NEPTUNE]

def main():
    planet = EARTH
    centralbody = SUN
    planet.printOrbitingValues()
    print("\nOrbiting: \n")
    centralbody.printCentralBodyValues()

if __name__ == "__main__":
    main()