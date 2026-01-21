class AerodynamicsModel:
    def __init__(self, cl=2.5, cd=1.0, frontal_area=2.0, air_density=1.225):
        """
        Aerodynamics parameters
        cl: lift coefficient (negative for downforce)
        cd: drag coefficient  
        frontal_area: m²
        air_density: kg/m³
        """
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