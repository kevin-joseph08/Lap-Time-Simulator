import numpy as np

class LapTimeSolver:
    def __init__(self, track, vehicle, tire_model, aero_model, powertrain_model):
        self.track = track
        self.vehicle = vehicle
        self.tire_model = tire_model
        self.aero_model = aero_model
        self.powertrain_model = powertrain_model
        
    def solve(self):
        """Solve for optimal speed profile"""
        n_segments = len(self.track.distances)
        velocities = np.zeros(n_segments)
        
        # Forward pass - acceleration limited
        velocities = self._forward_pass(velocities)
        
        # Backward pass - braking limited  
        velocities = self._backward_pass(velocities)
        
        return velocities
    
    def _forward_pass(self, velocities):
        """Forward pass applying acceleration and cornering limits"""
        for i in range(len(velocities)):
            if i == 0:
                velocities[i] = 0.1  # Start with small velocity
            else:
                # Previous velocity
                v_prev = velocities[i-1]
                ds = self.track.get_segment_length(i-1)
                
                # Calculate forces
                normal_force = self._get_normal_force(v_prev)
                engine_force = self.powertrain_model.engine_force(self.vehicle)
                drag_force = self.aero_model.drag(v_prev)
                
                # Net acceleration
                net_force = engine_force - drag_force
                acceleration = net_force / self.vehicle.mass
                
                # Velocity from acceleration
                v_accel = np.sqrt(v_prev**2 + 2 * acceleration * ds)
                velocities[i] = v_accel
            
            # Apply cornering limit
            radius = self.track.get_radius(i)
            normal_force = self._get_normal_force(velocities[i])
            v_corner = self.tire_model.max_cornering_speed(
                radius, normal_force, self.vehicle.mass)
            
            velocities[i] = min(velocities[i], v_corner)
        
        return velocities
    
    def _backward_pass(self, velocities):
        """Backward pass ensuring braking feasibility"""
        for i in range(len(velocities)-2, -1, -1):
            v_next = velocities[i+1]
            ds = self.track.get_segment_length(i)
            
            # Maximum braking deceleration
            normal_force = self._get_normal_force(velocities[i])
            brake_decel = self.vehicle.get_brake_acceleration_max(
                normal_force, self.tire_model.mu)
            
            # Maximum velocity to brake to v_next
            v_brake = np.sqrt(v_next**2 + 2 * brake_decel * ds)
            
            velocities[i] = min(velocities[i], v_brake)
        
        return velocities
    
    def _get_normal_force(self, velocity):
        """Calculate normal force including downforce"""
        weight = self.vehicle.mass * 9.81
        downforce = self.aero_model.downforce(velocity)
        return weight + downforce
    
    def calculate_lap_time(self, velocities):
        """Calculate total lap time from velocity profile"""
        total_time = 0
        for i in range(len(velocities)):
            ds = self.track.get_segment_length(i)
            dt = ds / max(velocities[i], 0.1)  # Avoid division by zero
            total_time += dt
        return total_time