from decimal import Decimal
import numpy as np

class Earth():
    def __init__(self):
        self.name = "Earth"
        self.aphelion = Decimal("1.017")
        self.perihelion = Decimal("0.983")
        self.semimajor_axis = Decimal((self.aphelion + self.perihelion)/2)
        self.focal_distance = Decimal(self.aphelion - self.semimajor_axis)
        self.semiminor_axis = Decimal(round(np.sqrt(self.semimajor_axis**2 - self.focal_distance**2), 10))
        self.eccentricity = Decimal(self.focal_distance/self.semimajor_axis)
        self.referenceRadius = Decimal(round(self.semiminor_axis**2 / self.semimajor_axis, 10))

def main():
    earth = Earth()
    print("Planet: " + earth.name)
    print(f"Aphelion: {earth.aphelion} au")
    print(f"Perihelion: {earth.perihelion} au")
    print(f"Semimajor - axis: {earth.semimajor_axis} au")
    print(f"Focal Distance: {earth.focal_distance} au")
    print(f"Semiminor - axis: {earth.semiminor_axis} au")
    print(f"Eccentricity: {earth.eccentricity}")
    print(f"Reference Radius: {earth.referenceRadius}")

if __name__ == "__main__":
    main()