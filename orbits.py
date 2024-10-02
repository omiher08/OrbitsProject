import planets
import numpy as np
import matplotlib.pyplot as plt
import random

def cartesian_coordinates(planet, ax):
    n_points = 10000
    x = np.linspace(-planet.semimajor_axis, planet.semimajor_axis, n_points)
    y = planet.semiminor_axis * np.sqrt(1-(x**2/planet.semimajor_axis**2))
    ax.plot(x, y, color="#2f7bf5")
    ax.plot(x, -y, color="#2f7bf5")
    ax.plot(-planet.focal_distance, 0, marker="o", markersize=8, label="Sun", color="#dbc70d")
    point = random.choice(range(0,n_points))
    y_axis_of_earth = random.choice(["+", "-"])
    if y_axis_of_earth == "+":
        ax.plot(x[point], y[point], marker="o", markersize=8, label=f"{planet.name}", color="green")
    else:
        ax.plot(x[point], -y[point], marker="o", markersize=8, label=f"{planet.name}", color="green")
    ax.axis("equal")
    ax.set_title(f"{planet.name}'s Orbit in cartesian coordinates", fontsize=8)
    ax.set_xlabel("X (au)")
    ax.set_ylabel("Y (au)")
    ax.grid()
    ax.legend()

def polar_coordinates(planet, ax):
    n_points = 10000
    ax.set_title(f"{planet.name}'s Orbit in polar coordinates", fontsize=8)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

def main():
    planet = planets.Earth()
    fig = plt.figure()
    s1 = fig.add_subplot(2, 2, 1)
    s2 = fig.add_subplot(2, 2, 2, polar=True)
    s3 = fig.add_subplot(2, 2, 3)
    s4 = fig.add_subplot(2, 2, 4)
    cartesian_coordinates(planet, s1)
    polar_coordinates(planet, s2)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()