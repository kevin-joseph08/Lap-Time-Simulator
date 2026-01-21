class Vehicle:
    def __init__(self, mass, wheel_radius=0.33, drivetrain_efficiency=0.9, 
                 brake_force_max=15000):
        """
        Vehicle parameters
        mass: kg
        wheel_radius: m
        drivetrain_efficiency: dimensionless
        brake_force_max: N
        """
        self.mass = mass
        self.wheel_radius = wheel_radius
        self.drivetrain_efficiency = drivetrain_efficiency
        self.brake_force_max = brake_force_max
    
    def get_brake_acceleration_max(self, normal_force, mu):
        """Maximum braking acceleration based on tire friction"""
        return min(mu * normal_force / self.mass, 
                  self.brake_force_max / self.mass)