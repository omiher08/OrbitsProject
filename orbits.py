import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from objects import *

def verlet(current_position, last_position, acceleration, deltaT):
    return 2*current_position-last_position+acceleration*deltaT**2

def acceleration(centralBodymass, x_difference, y_difference, distance):
    a_x = ((G*centralBodymass*(x_difference))/distance**3) * 86400**2/UA_meters #UA/Day**2
    a_y = ((G*centralBodymass*(y_difference))/distance**3)* 86400**2/UA_meters #UA/Day**2
    return a_x, a_y

def is_decimal(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
    
def generate_personalized():
    object_name = input("\nEnter object's name: ").strip().capitalize()
    while True:
        object_aphelion = input("\nEnter object's aphelion in au (Use '.' for decimals): ").strip().capitalize()
        ok = is_decimal(object_aphelion)
        if ok:
            break
        else:
            print("Not a valid aphelion")
    while True:
        object_perihelion = input("\nEnter object's perihelion in au (Use '.' for decimals): ").strip().capitalize()
        ok = is_decimal(object_perihelion)
        if ok:
            break
        else:
            print("Not a valid perihelion")
    orbitingBody = OrbitingBody(object_name, "black", object_aphelion, object_perihelion)
    centralBody_name = input("\nEnter central body's name (body that your object orbits) (Write 'Sun' if the central body is the sun): ").strip().capitalize()
    if centralBody_name.upper() == "SUN":
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
    ax.set_xlim(min(x)-Decimal(0.5), max(x)+Decimal(0.5))
    ax.set_ylim(min(-y)-Decimal(0.5), max(y)+Decimal(0.5))
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f"{orbitingBody.name}'s Orbit in cartesian coordinates", fontsize=10)
    ax.set_xlabel("X (au)")
    ax.set_ylabel("Y (au)")
    ax.grid()
    return x, y

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
    
def simulation(orbitingBody, centralBody, ax, fig):
    dt = 1
    perihelion_in_m = orbitingBody.perihelion * UA_meters
    aphelion_in_m = orbitingBody.aphelion * UA_meters
    x_0 = orbitingBody.semimajor_axis
    vx_0 = 0
    x_1 = Decimal(x_0+vx_0*dt)
    y_0 = 0
    vy_0 = Decimal((np.sqrt((2*G*centralBody.mass*(-1/perihelion_in_m + 1/aphelion_in_m))/(1-((aphelion_in_m**2)/(perihelion_in_m**2))))) * (Decimal(86400)/UA_meters)) #au/dia
    y_1 = Decimal(y_0+vy_0*dt)
    x_positions = [x_0, x_1]
    y_positions = [y_0, y_1]
    orbital_period = (2*Decimal(np.pi)*np.sqrt(((orbitingBody.semimajor_axis*UA_meters)**3)/(G*centralBody.mass)))/86400 #In Days
       
    for day in range(int(orbital_period)):
        current_x = x_positions[-1]
        current_y = y_positions[-1]
        previous_x = x_positions[-2]
        previous_y = y_positions[-2]
        distance_x = (-orbitingBody.focal_distance-current_x) * UA_meters #In meters
        distance_y = (0-current_y) * UA_meters #In meters
        distance = Decimal(np.sqrt(distance_x**2+distance_y**2)) #In meters
        a_x, a_y = acceleration(centralBody.mass, distance_x, distance_y, distance)
        next_x = verlet(current_x, previous_x, a_x, dt)
        next_y = verlet(current_y, previous_y, a_y, dt)
        x_positions.append(next_x)
        y_positions.append(next_y)
        
    total_points = len(x_positions)
    desired_points = 1100
    
    if total_points > desired_points:
        step = total_points // desired_points + 1
        reduced_x_positions = x_positions[::step]
        reduced_y_positions = y_positions[::step]
        reduced_x_positions.append(x_positions[-1])  # Ensure the last point is included
        reduced_y_positions.append(y_positions[-1])  # Ensure the last point is included
    else:
        reduced_x_positions = x_positions
        reduced_y_positions = y_positions
        
    planet_position, = ax.plot([], [], "o", color=orbitingBody.color, markersize=8)
    planet_orbit, = ax.plot([], [], color="#2f7bf5")
    
    def animate(i):
        x = reduced_x_positions[i]
        y = reduced_y_positions[i]
        planet_position.set_data([x], [y])
        
        planet_orbit.set_data(reduced_x_positions[:i], reduced_y_positions[:i])
        
        return planet_orbit, planet_position
    
    def calculate_interval(n):
        if n <= 230:
            return 12
        elif n <= 360:
            return 8
        elif n <= 500:
            return 2
        else:
            return 0.1
    
    set_interval = calculate_interval(len(reduced_x_positions))
    
    ani = animation.FuncAnimation(fig, animate, frames=len(reduced_x_positions), blit=True, interval=set_interval, repeat=True)
    ax.plot(-orbitingBody.focal_distance, 0, marker="o", markersize=8, color=centralBody.color)    
    ax.set_xlim(min(x_positions)-Decimal(0.5), max(x_positions)+Decimal(0.5))
    ax.set_ylim(min(y_positions)-Decimal(0.5), max(y_positions)+Decimal(0.5))
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f"{orbitingBody.name}'s Orbit using Gravitational Equations and Verlet", fontsize=10)
    ax.set_xlabel("X (au)")
    ax.set_ylabel("Y (au)")
    ax.grid()
    return ani, x_positions, y_positions

def overlapping(orbitingBody, centralBody, ax, fig, geometric_x, geometric_y, verlet_x, verlet_y):
    ax.plot(geometric_x, geometric_y, color="#24d6b0", label="Geometric Orbit in Comparison")
    ax.plot(verlet_x, verlet_y, color="#ff0000", label="Gravitational Equations and Verlet Orbit in Comparison")
    ax.plot(-orbitingBody.focal_distance, 0, marker="o", markersize=8, color=centralBody.color)
    ax.set_xlim(min(verlet_x)-Decimal(0.5), max(verlet_x)+Decimal(0.5))
    ax.set_ylim(min(verlet_y)-Decimal(0.5), max(verlet_y)+Decimal(0.5))
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f"{orbitingBody.name}'s Orbits Comparison", fontsize=10)
    ax.set_xlabel("X (au)")
    ax.set_ylabel("Y (au)")
    ax.grid()
    

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
    geometric_x_positions, geometric_y_positions = cartesian_coordinates(orbitingBody, centralBody, s1)
    polar_coordinates(orbitingBody, centralBody, s2)
    ani, verlet_x_positions, verlet_y_positions = simulation(orbitingBody, centralBody, s3, fig)
    overlapping(orbitingBody, centralBody, s4, fig, geometric_x_positions, geometric_y_positions, verlet_x_positions, verlet_y_positions)
    fig.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()