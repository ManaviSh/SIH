import math
import numpy as np
class vehicle:
#    def __init__(self, M = 1650, g = 9.8, f = 0.011, eff = 0.9, C_air =  0.55, A_air = 6.6, R_roll = 0.05):
#        self.M = M
#        self.g = g
#        self.f = f
#        self.eff = eff
#        self.C_air = C_air
#        self.A_air = A_air
#        self.R_roll = R_roll
#    def Power_Required(self, velocity, cos_theta, sin_theta, acceleration):
#        P_req = np.zeros(132124)
#        P_req = 0.001*velocity*((self.M*self.f*self.g*cos_theta) + (self.M*self.g*sin_theta) + (self.C_air*self.A_air*velocity*velocity)/21.15 + (self.R_roll*self.M*acceleration))/self.eff
#        return P_req
#    
#    
#    
#    
#    
##    class need_energy():
    def __init__(self):
        self.mass = 2000 #kg
        self.mass_factor = 1.05
        #self.acceleration = 0 # m^2 / s
        self.coeff_roll_R = 0.02  # coefficient of rolling resistance
        self.air_density = 1.225 # kg/m^3
        self.front_area = 2 # m^2
        self.aero_drag_coff = 0.5
        self.wind_speed = 0 # m/s
        self.road_angle = 0 # angle

    def Power_Required(self, velocity, cos_theta, sin_theta, acceleration):  # V is driving speed
        #self.road_angle = angle
        #rad = math.radians(angle)
        p1 = (self.mass_factor * self.mass * acceleration) + (self.mass * 9.8 * self.coeff_roll_R * cos_theta)
        p2 = 0.5 * self.air_density * self.front_area * self.aero_drag_coff * ((velocity - self.wind_speed)**2)
        p3 = self.mass * 9.8 * sin_theta

        P_req = 0.001*(p1 + p2 + p3) * velocity   # Watt
        return P_req