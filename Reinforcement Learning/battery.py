import math
import  numpy as np
class battery:
    def __init__(self, R_i, delta, N = 88, C = 16, k = 1.2): #mitsubishi MIEV, li-ion
        self.N = N #nuber of cells
        self.C = C #Capaciy of battery
        self.R_i = R_i #Internal Resistance
        self.k = k #Peukers constant
        self.delta = delta #dicharge current delta

    def Find_OCV(self, battery_type, DoD): # function for finding open circuit voltage separately delta
        if battery_type == 0: #lead-acid
            E = self.N * (2.15 - DoD * 0.15)
        else: #nickel - cadmium
            E = (-8.2816*DoD**7+23.5749*DoD**6-30*DoD**5+23.7053*DoD**4-12.5877*DoD**3+4.1315*DoD**2-0.8658*DoD+1.37)*N
        return E
    def send_DoD(self, P, num = 585):
        SOC = 100
        SOC += SOC + P/self.C
        DoD = 100 - SOC
        return DoD