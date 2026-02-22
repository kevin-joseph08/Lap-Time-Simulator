from validation import ValidationError, validate_positive

class PowertrainModel:
    def __init__(self, max_torque=400, gear_ratio=3.5):
        """
        Simplified powertrain model
        max_torque: Nm
        gear_ratio: dimensionless
        """
        validate_positive(max_torque, "Maximum torque")
        validate_positive(gear_ratio, "Gear ratio")
        
        if max_torque > 2000:
            raise ValidationError(f"Maximum torque {max_torque} Nm exceeds reasonable limit (2000 Nm)")
        if gear_ratio > 20:
            raise ValidationError(f"Gear ratio {gear_ratio} exceeds reasonable limit (20)")
        
        self.max_torque = max_torque
        self.gear_ratio = gear_ratio
    
    def engine_force(self, vehicle):
        """Calculate engine force at wheels"""
        return (self.max_torque * self.gear_ratio * 
                vehicle.drivetrain_efficiency / vehicle.wheel_radius)