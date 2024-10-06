from decimal import Decimal
import numpy as np

class OrbitingObject():
    def __init__(self, aphelion, perihelion):
        self.semimajor_axis = round(Decimal((aphelion + perihelion)/2), 10)
        self.focal_distance = round(Decimal(aphelion - self.semimajor_axis), 10)
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
    def __init__(self):
        pass
    def printCentralBodyValues(self):
        print(f"Central Body: {self.name}")
        print(f"Color: {self.color}")

class Sun(CentralBody):
    def __init__(self):
        self.name = "Sun"
        self.color = "#dbc70d"

class Earth(OrbitingObject):
    def __init__(self):
        self.name = "Earth"
        self.color = "green"
        self.aphelion = Decimal("1.017")
        self.perihelion = Decimal("0.983")
        super().__init__(self.aphelion, self.perihelion)

class Mercury(OrbitingObject):
    def __init__(self):
        self.name = "Mercury"
        self.color = "#b08137"
        self.aphelion = Decimal("0.4667007938")
        self.perihelion = Decimal("0.3074977524")
        super().__init__(self.aphelion, self.perihelion)

def KmToAu(aphelion_in_km, perihelion_in_km):
    one_au = Decimal("149597870.7")
    aphelion_in_au = aphelion_in_km / one_au
    perihelion_in_au = perihelion_in_km / one_au
    return round(aphelion_in_au, 10), round(perihelion_in_au, 10)

def main():
    planet = Earth()
    centralbody = Sun()
    planet.printOrbitingValues()
    print("\nOrbiting: \n")
    centralbody.printCentralBodyValues()

if __name__ == "__main__":
    main()