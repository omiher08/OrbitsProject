from objects import EARTH, SUN, G, UA_meters
from orbits import verlet
import numpy as np
from decimal import Decimal
import matplotlib.animation as animation

def acceleration(centralBodymass, x_difference, y_difference, distance):
    a_x = ((G*centralBodymass*(x_difference))/distance**3) * 86400**2/UA_meters #Ua/Dia**2
    a_y = ((G*centralBodymass*(y_difference))/distance**3)* 86400**2/UA_meters #Ua/Dia**2
    return a_x, a_y

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
       
    for day in range(int(orbital_period)+1):
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
        
    planet_position, = ax.plot([], [], color=orbitingBody.color)
    
    def animate(i):
        x = x_positions[:i]
        y = y_positions[:i]
        planet_position.set_data(x, y)
        return planet_position,
    
    ax.set_xlim(min(x_positions), max(x_positions))
    ax.set_ylim(min(y_positions), max(y_positions))
    ani = animation.FuncAnimation(fig, animate, int(orbital_period)+3, blit=True, interval=0.1, repeat=False)
    
    #ax.plot(x_positions, y_positions, color="#2f7bf5") #Variar color
    ax.plot(-orbitingBody.focal_distance, 0, marker="o", markersize=8, color=centralBody.color)
    ax.grid()
    ax.set_aspect('equal', adjustable='box')
    return ani

#1. Intervalo varia dependiendo de la cantidad de puntos
#2. Calcular antes y simplemente mostrar
#3. Formula para la relación de aspecto