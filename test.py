from objects import EARTH, SUN, G, UA
import numpy as np
from decimal import Decimal

def simulation(orbitingBody = EARTH, centralBody = SUN, ax = None):
    dt = 1
    perihelion_in_m = orbitingBody.perihelion * UA
    aphelion_in_m = orbitingBody.aphelion * UA
    x_0 = orbitingBody.semimajor_axis
    vx_0 = 0
    x_1 = x_0+vx_0*dt
    y_0 = 0
    vy_0 = (np.sqrt((2*G*centralBody.mass*(-1/perihelion_in_m + 1/aphelion_in_m))/(1-((aphelion_in_m**2)/(perihelion_in_m**2))))) * (Decimal(86400)/UA)
    y_1 = y_0+vy_0*dt
    x_positions = [x_0, x_1]
    y_positions = [y_0, y_1]
    print(x_positions, y_positions)

#Distancia = np.sqrt((x_sol - x_planeta_actual)**2 + (y_sol - y_planeta_actual)**2)

simulation()