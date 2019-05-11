import pandas as pd
import numpy as np
import math
class reward:
    def __init__(self, state_length = 63, action_length = 116):
        self.state_length = state_length
        self.action_length = action_length
    
    def get_reward(self, velocity, theta):
        mass = 2000 #kg
        mass_factor = 1.05
        acceleration = 0 # m^2 / s
        coeff_roll_R = 0.02  # coefficient of rolling resistance
        air_density = 1.225 # kg/m^3
        front_area = 2 # m^2
        aero_drag_coff = 0.5
        wind_speed = 0 # m/s
        road_angle = 0 # angle
        p1 = (mass_factor * mass * acceleration) + (mass * 9.8 * coeff_roll_R * math.cos(theta))
        p2 = 0.5 * air_density * front_area * aero_drag_coff * ((velocity - wind_speed)**2)
        p3 = mass * 9.8 * math.sin(theta)
        P_req = 0.001*(p1 + p2 + p3) * velocity   # Watt
        if P_req ==0:
            return 0
        else:
            return 1/P_req
