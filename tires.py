import numpy as np

class TireModel:
    def __init__(self, mu=1.2):
        """
        Simplified tire model
        mu: coefficient of friction
        """
        self.mu = mu
    
    def max_lateral_force(self, normal_force, longitudinal_force=0):
        """Maximum lateral force given normal force and longitudinal force"""
        max_total = self.mu * normal_force
        return np.sqrt(max_total**2 - longitudinal_force**2)
    
    def max_cornering_speed(self, radius, normal_force, mass):
        """Maximum cornering speed for given radius and normal force"""
        if radius == float('inf'):
            return float('inf')
        return np.sqrt(self.mu * normal_force * radius / mass)