class PowertrainModel:
    def __init__(self, max_torque=400, gear_ratio=3.5):
        """
        Simplified powertrain model
        max_torque: Nm
        gear_ratio: dimensionless
        """
        self.max_torque = max_torque
        self.gear_ratio = gear_ratio
    
    def engine_force(self, vehicle):
        """Calculate engine force at wheels"""
        return (self.max_torque * self.gear_ratio * 
                vehicle.drivetrain_efficiency / vehicle.wheel_radius)