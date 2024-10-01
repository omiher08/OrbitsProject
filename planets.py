from decimal import Decimal
import numpy as np

class Earth():
    def __init__(self):
        self.name = "Earth"
        self.aphelion = Decimal("1.017")
        self.perihelion = Decimal("0.983")
        self.semimajor_axis = Decimal((self.aphelion + self.perihelion)/2)
        self.focal_distance = Decimal(self.aphelion - self.semimajor_axis)
        self.semiminor_axis = round(Decimal(np.sqrt(self.semimajor_axis**2 - self.focal_distance**2)), 10)
        self.eccentricity = Decimal(self.focal_distance/self.semimajor_axis)
        self.referenceRadius = round(Decimal(self.semiminor_axis**2 / self.semimajor_axis), 10)

def main():
    planet = Earth()
    print("Planet: " + planet.name)
    print(f"Aphelion: {planet.aphelion} au")
    print(f"Perihelion: {planet.perihelion} au")
    print(f"Semimajor - axis: {planet.semimajor_axis} au")
    print(f"Focal Distance: {planet.focal_distance} au")
    print(f"Semiminor - axis: {planet.semiminor_axis} au")
    print(f"Eccentricity: {planet.eccentricity}")
    print(f"Reference Radius: {planet.referenceRadius}")

if __name__ == "__main__":
    main()