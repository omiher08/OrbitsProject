from decimal import Decimal
import numpy as np

class OrbitingBody():
    def __init__(self, name, color, aphelion, perihelion):
        self.name = name
        self.color = color
        self.aphelion = Decimal(aphelion)
        self.perihelion = Decimal(perihelion)
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

class CentralBody():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def printCentralBodyValues(self):
        print(f"Central Body: {self.name}")
        print(f"Color: {self.color}")

def KmToAu(aphelion_in_km, perihelion_in_km):
    one_au = Decimal("149597870.7")
    aphelion_in_au = aphelion_in_km / one_au
    perihelion_in_au = perihelion_in_km / one_au
    return round(aphelion_in_au, 10), round(perihelion_in_au, 10)

EARTH = OrbitingBody("Earth", "green", "1.017", "0.983")
MERCURY = OrbitingBody("Mercury", "#b08137", "0.466", "0.307")
SUN = CentralBody("Sun", "#dbc70d")

def main():
    planet = EARTH
    centralbody = SUN
    planet.printOrbitingValues()
    print("\nOrbiting: \n")
    centralbody.printCentralBodyValues()

if __name__ == "__main__":
    main()