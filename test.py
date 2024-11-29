from objects import EARTH, SUN, G, UA_meters
import numpy as np
from decimal import Decimal

def simulation(orbitingBody = EARTH, centralBody = SUN, ax = None):
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
    
    for day in range(int(orbital_period) + 2): # +2 ya que range es exclusivo
        current_x = x_positions[-1]
        current_y = y_positions[-1]
        previous_x = x_positions[-2]
        previous_y = y_positions[-2]
        distance = Decimal(np.sqrt((-orbitingBody.focal_distance-current_x)**2+(0-current_y)**2))
        print(day)

simulation()