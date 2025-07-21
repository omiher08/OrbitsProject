# Modeling and Simulation of Planetary Orbits
## 🛰️ Project Description
This project seeks to answer a fundamental question: is it possible to accurately plot a planet's orbit knowing only its aphelion, perihelion, and mass?

To validate this, a dual approach is followed:

Geometric Model: The geometric equation of the ellipse is used to construct the orbital trajectory of a planet in Cartesian and polar coordinates.

Dynamic Simulation: The Verlet numerical integration method is implemented to simulate the planet's movement under the Sun's gravitational influence.

The final goal is to overlay both plots to compare and verify if the dynamic model (Verlet) matches the perfect geometric ellipse derived from the initial data.

## 📂 File Descriptions
objects.py: Defines the class for celestial bodies (planets and the Sun). Here, objects are instantiated with their key attributes: mass, color, aphelion, and perihelion, from which eccentricity and other orbital elements are calculated.

main_simulation.py: The heart of the project. It implements and plots the geometric ellipse (both in cartesian and polar coordinates) and the dynamic trajectory calculated with the Verlet method. Its main function is to overlay both results for a direct visual comparison.

solar_system_orbital_representation.py: An additional script that displays all planetary orbits together in polar coordinates. It is ideal for a global comparative view of the shapes and sizes of the solar system's orbits.

requirements.txt: A text file with the necessary Python dependencies to run the project.

## ⚙️ Installation
To run this project on your local machine, follow these steps.

Clone the repository:

git clone https://github.com/omiher08/planetary-orbit-plotter

cd planetary-orbit-plotter

Install the dependencies:

pip install -r requirements.txt

## ▶️ Usage
To run the main simulation and compare the methods, use the following command:

python main_simulation.py

If you want to see the representation of all the solar system orbits together:

python solar_system_orbital_representation.py
