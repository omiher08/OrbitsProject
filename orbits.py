from objects import *
import numpy as np
import matplotlib.pyplot as plt
import random

def cartesian_coordinates(orbitingBody, centralBody, ax):
    n_points = 10000
    x = np.linspace(-orbitingBody.semimajor_axis, orbitingBody.semimajor_axis, n_points)
    y = orbitingBody.semiminor_axis * np.sqrt(1-(x**2/orbitingBody.semimajor_axis**2))
    ax.plot(x, y, color="#2f7bf5")
    ax.plot(x, -y, color="#2f7bf5")
    ax.plot(-orbitingBody.focal_distance, 0, marker="o", markersize=8, label=centralBody.name, color=centralBody.color)
    point = random.choice(range(0,n_points))
    x_point, y_point = x[point], y[point]
    y_axis_of_earth = random.choice(["+", "-"])
    if y_axis_of_earth == "-":
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
    theta_point, r_point = theta[point], r[point]
    ax.plot(theta_point, r_point, marker="o", markersize=8, color=f"{orbitingBody.color}")
    ax.set_title(f"{orbitingBody.name}'s Orbit in polar coordinates", fontsize=10)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

def main():
    orbitingBody = EARTH
    centralBody = SUN
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