from decimal import Decimal
import numpy as np

class CelestialObject():
    def __init__(self, aphelion, perihelion):
        self.semimajor_axis = Decimal((aphelion + perihelion)/2)
        self.focal_distance = Decimal(aphelion - self.semimajor_axis)
        self.semiminor_axis = Decimal(np.sqrt(self.semimajor_axis**2 - self.focal_distance**2))
        self.eccentricity = Decimal(self.focal_distance/self.semimajor_axis)
        self.referenceRadius = Decimal(self.semiminor_axis**2 / self.semimajor_axis)

class Earth(CelestialObject):
    def __init__(self):
        self.name = "Earth"
        self.color = "green"
        self.aphelion = Decimal("1.017")
        self.perihelion = Decimal("0.983")
        super().__init__(self.aphelion, self.perihelion)

def main():
    planet = Earth()
    print("Planet: " + planet.name)
    print(f"Color: {planet.color}")
    print(f"Aphelion: {planet.aphelion} au")
    print(f"Perihelion: {planet.perihelion} au")
    print(f"Semimajor - axis: {planet.semimajor_axis} au")
    print(f"Focal Distance: {planet.focal_distance} au")
    print(f"Semiminor - axis: {planet.semiminor_axis} au")
    print(f"Eccentricity: {planet.eccentricity}")
    print(f"Reference Radius: {planet.referenceRadius}")

if __name__ == "__main__":
    main()