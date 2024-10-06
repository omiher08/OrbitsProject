from objects import *
import numpy as np
import matplotlib.pyplot as plt
import random

def cartesian_coordinates(orbitingobject, centralbody, ax):
    n_points = 10000
    x = np.linspace(-orbitingobject.semimajor_axis, orbitingobject.semimajor_axis, n_points)
    y = orbitingobject.semiminor_axis * np.sqrt(1-(x**2/orbitingobject.semimajor_axis**2))
    ax.plot(x, y, color="#2f7bf5")
    ax.plot(x, -y, color="#2f7bf5")
    ax.plot(-orbitingobject.focal_distance, 0, marker="o", markersize=8, label=centralbody.name, color=centralbody.color)
    point = random.choice(range(0,n_points))
    x_point, y_point = x[point], y[point]
    y_axis_of_earth = random.choice(["+", "-"])
    if y_axis_of_earth == "-":
        y_point = -y_point
    ax.plot(x_point, y_point, marker="o", markersize=8, label=f"{orbitingobject.name}", color=f"{orbitingobject.color}")
    ax.axis("equal")
    ax.set_title(f"{orbitingobject.name}'s Orbit in cartesian coordinates", fontsize=10)
    ax.set_xlabel("X (au)")
    ax.set_ylabel("Y (au)")
    ax.grid()

def polar_coordinates(orbitingobject, centralbody, ax):
    n_points = 10000
    theta = np.linspace(0, 2*np.pi, n_points)
    r = float(orbitingobject.referenceRadius) / (1 + float(orbitingobject.eccentricity) * np.cos(theta))
    ax.plot(theta, r, color="#2f7bf5")
    ax.plot(0, 0, marker="o", markersize=8, color=centralbody.color)
    point = random.choice(range(0,n_points))
    theta_point, r_point = theta[point], r[point]
    ax.plot(theta_point, r_point, marker="o", markersize=8, color=f"{orbitingobject.color}")
    ax.set_title(f"{orbitingobject.name}'s Orbit in polar coordinates", fontsize=10)    
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

def main():
    orbitingobject = Mercury()
    centralbody = Sun()
    orbitingobject.printOrbitingValues()
    fig = plt.figure()
    s1 = fig.add_subplot(2, 2, 1)
    s2 = fig.add_subplot(2, 2, 2, polar=True)
    s3 = fig.add_subplot(2, 2, 3)
    s4 = fig.add_subplot(2, 2, 4)
    cartesian_coordinates(orbitingobject, centralbody, s1)
    polar_coordinates(orbitingobject, centralbody, s2)
    fig.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()