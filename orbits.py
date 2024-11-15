import numpy as np
import matplotlib.pyplot as plt
import random
from objects import *

dt = 1

def verlet(current_position, last_position, acceleration, deltaT):
    return 2*current_position-last_position+acceleration*deltaT**2

def is_decimal(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
    
def generate_personalized():
    object_name = input("\nEnter object's name: ").strip().capitalize()
    while True:
        object_aphelion = input("Enter object's aphelion in au (Use '.' for decimals): ").strip().capitalize()
        ok = is_decimal(object_aphelion)
        if ok:
            break
        else:
            print("\nNot a valid aphelion")
    while True:
        object_perihelion = input("Enter object's perihelion in au (Use '.' for decimals): ").strip().capitalize()
        ok = is_decimal(object_perihelion)
        if ok:
            break
        else:
            print("\nNot a valid perihelion")
    orbitingBody = OrbitingBody(object_name, "black", object_aphelion, object_perihelion)
    centralBody_name = input("\nEnter central body's name (body that your object orbits) (Write 'Sun' if the central body is the sun): ").strip().capitalize()
    if centralBody_name == "Sun":
        centralBody = SUN
    else:
        centralBody = CentralBody(centralBody_name, "#918c8c")
    
    return orbitingBody, centralBody

def cartesian_coordinates(orbitingBody, centralBody, ax):
    n_points = 10000
    x = np.linspace(-orbitingBody.semimajor_axis, orbitingBody.semimajor_axis, n_points)
    y = orbitingBody.semiminor_axis * np.sqrt(1-(x**2/orbitingBody.semimajor_axis**2))
    ax.plot(x, y, color="#2f7bf5")
    ax.plot(x, -y, color="#2f7bf5")
    ax.plot(-orbitingBody.focal_distance, 0, marker="o", markersize=8, label=centralBody.name, color=centralBody.color)
    point = random.choice(range(0,n_points))
    x_point, y_point = x[point], y[point]
    y_axis_of_object = random.choice(["+", "-"])
    if y_axis_of_object == "-":
        y_point = -y_point
    ax.plot(x_point, y_point, marker="o", markersize=8, label=f"{orbitingBody.name}", color=f"{orbitingBody.color}")
    ax.axis("equal")
    ax.set_title(f"{orbitingBody.name}'s Orbit in cartesian coordinates", fontsize=10)
    ax.set_xlabel("X (au)")
    ax.set_ylabel("Y (au)")
    ax.grid()

def polar_coordinates(orbitingBody, centralBody, ax):
    n_points = 10000
    theta = np.linspace(0, 2*np.pi, n_points)
    r = float(orbitingBody.referenceRadius) / (1 + float(orbitingBody.eccentricity) * np.cos(theta))
    ax.plot(theta, r, color="#2f7bf5")
    ax.plot(0, 0, marker="o", markersize=8, color=centralBody.color)
    point = random.choice(range(0,n_points))
    ax.plot(theta[point], r[point], marker="o", markersize=8, color=f"{orbitingBody.color}")
    ax.set_title(f"{orbitingBody.name}'s Orbit in polar coordinates", fontsize=10)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

def main():
    while True:
        try:
            ask = int(input("""Which object would you like to graph?
                            
1. Mercury
                            
2. Venus
                            
3. Earth
                            
4. Mars
                            
5. Jupiter
                            
6. Saturn
                            
7. Uranus
                            
8. Neptune
                            
9. Custom
                            
Choose (1-9): """).strip())
            if 0 < ask < 10:
                if ask == 9:
                    orbitingBody, centralBody = generate_personalized()
                else:
                    orbitingBody = PLANETS[ask-1]
                    centralBody = SUN
                print()
                break
            else:
                print("\nYou must enter a number between 1 and 9.")
        except ValueError:
            print("\nThat's not a valid input.")
    orbitingBody.printOrbitingValues()
    fig = plt.figure()
    s1 = fig.add_subplot(2, 2, 1)
    s2 = fig.add_subplot(2, 2, 2, polar=True)
    s3 = fig.add_subplot(2, 2, 3)
    s4 = fig.add_subplot(2, 2, 4)
    cartesian_coordinates(orbitingBody, centralBody, s1)
    polar_coordinates(orbitingBody, centralBody, s2)
    fig.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()