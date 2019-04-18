import math
import numpy as np
class vehicle:
    def __init__(self, M = 1650, g = 9.8, f = 0.011, eff = 0.9, C_air =  0.55, A_air = 6.6, R_roll = 0.05):
        self.M = M
        self.g = g
        self.f = f
        self.eff = eff
        self.C_air = C_air
        self.A_air = A_air
        self.R_roll = R_roll
    def Power_Required(self, velocity, cos_theta, sin_theta, acceleration):
        P_req = np.zeros(585)
        P_req = 0.001*velocity*((self.M*self.f*self.g*cos_theta) + (self.M*self.g*sin_theta) + (self.C_air*self.A_air*velocity*velocity)/21.15 + (self.R_roll*self.M*acceleration))/self.eff
        return P_req