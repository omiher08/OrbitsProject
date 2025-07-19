import numpy as np
import matplotlib.pyplot as plt
import random
from objects import *

def solarsystem(orbitingBody, ax):
    n_points = 10000
    theta = np.linspace(0, 2*np.pi, n_points)
    r = float(orbitingBody.referenceRadius) / (1 + float(orbitingBody.eccentricity) * np.cos(theta))
    ax.plot(theta, r, color=orbitingBody.color, linewidth=1.5)
    point = random.choice(range(0,n_points))
    ax.plot(theta[point], r[point], marker="o", markersize=3, label=orbitingBody.name, color=f"{orbitingBody.color}")

def main():
    fig = plt.figure()
    s1 = fig.add_subplot(1, 1, 1, polar=True)
    for planet in PLANETS:
        solarsystem(planet, s1)
    s1.plot(0, 0, marker="o", markersize=2, label=SUN.name, color=SUN.color)
    s1.grid(color='gray', linestyle='--', linewidth=0.5)
    s1.set_title("Solar system 2D representation")
    fig.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()