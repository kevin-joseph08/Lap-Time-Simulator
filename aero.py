from validation import ValidationError, validate_positive

class AerodynamicsModel:
    def __init__(self, cl=2.5, cd=1.0, frontal_area=2.0, air_density=1.225):
        """
        Aerodynamics parameters
        cl: lift coefficient (negative for downforce)
        cd: drag coefficient  
        frontal_area: m²
        air_density: kg/m³
        """
        validate_positive(cd, "Drag coefficient")
        validate_positive(frontal_area, "Frontal area")
        validate_positive(air_density, "Air density")
        
        if abs(cl) > 10:
            raise ValidationError(f"Lift coefficient {cl} exceeds realistic limit (|cl| <= 10)")
        if cd > 5:
            raise ValidationError(f"Drag coefficient {cd} exceeds realistic limit (5)")
        if frontal_area > 10:
            raise ValidationError(f"Frontal area {frontal_area} m^2 exceeds reasonable limit (10 m^2)")
        
        self.cl = cl
        self.cd = cd
        self.frontal_area = frontal_area
        self.air_density = air_density
    
    def downforce(self, velocity):
        """Downforce at given velocity"""
        return 0.5 * self.air_density * self.cl * self.frontal_area * velocity**2
    
    def drag(self, velocity):
        """Drag force at given velocity"""
        return 0.5 * self.air_density * self.cd * self.frontal_area * velocity**2