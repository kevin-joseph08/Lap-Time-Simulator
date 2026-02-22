from validation import ValidationError, validate_positive, validate_range

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
        validate_positive(mass, "Vehicle mass")
        validate_positive(wheel_radius, "Wheel radius")
        validate_range(drivetrain_efficiency, "Drivetrain efficiency", 0.1, 1.0)
        validate_positive(brake_force_max, "Maximum brake force")
        
        if mass > 10000:
            raise ValidationError(f"Vehicle mass {mass} kg exceeds reasonable limit (10000 kg)")
        if wheel_radius > 1.0:
            raise ValidationError(f"Wheel radius {wheel_radius} m exceeds reasonable limit (1.0 m)")
        
        self.mass = mass
        self.wheel_radius = wheel_radius
        self.drivetrain_efficiency = drivetrain_efficiency
        self.brake_force_max = brake_force_max
    
    def get_brake_acceleration_max(self, normal_force, mu):
        """Maximum braking acceleration based on tire friction"""
        return min(mu * normal_force / self.mass, 
                  self.brake_force_max / self.mass)