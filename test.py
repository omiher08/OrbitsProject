from objects import EARTH, SUN, G
import numpy as np
from decimal import Decimal

def simulation(orbitingBody = None, centralBody = None, ax = None):
    orbitingBody = EARTH
    centralBody = SUN
    perihelion_in_m = orbitingBody.perihelion * Decimal(1.496e11)
    aphelion_in_m = orbitingBody.aphelion * Decimal(1.496e11)
    x_0 = orbitingBody.semimajor_axis
    vx_0 = 0
    y_0 = 0
    vy_0 = np.sqrt((2*G*centralBody.mass*(-1/perihelion_in_m + 1/aphelion_in_m))/(1-((aphelion_in_m**2)/(perihelion_in_m**2))))
    print(vy_0)
    
simulation()