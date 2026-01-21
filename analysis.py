import numpy as np
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

class LapAnalysis:
    def __init__(self, track, velocities, lap_time):
        self.track = track
        self.velocities = velocities
        self.lap_time = lap_time
    
    def print_summary(self):
        """Print lap time summary"""
        max_speed = np.max(self.velocities) * 3.6  # Convert to km/h
        avg_speed = (self.track.total_length / self.lap_time) * 3.6
        
        print(f"Lap Time: {self.lap_time:.2f} seconds")
        print(f"Maximum Speed: {max_speed:.1f} km/h")
        print(f"Average Speed: {avg_speed:.1f} km/h")
    
    def plot_speed_profile(self):
        """Plot speed vs distance with track visualization"""
        if not HAS_MATPLOTLIB:
            print("Matplotlib not available - cannot create plots")
            return
            
        fig = plt.figure(figsize=(15, 10))
        
        # Speed profile
        plt.subplot(2, 2, 1)
        plt.plot(self.track.distances, self.velocities * 3.6)
        plt.xlabel('Distance (m)')
        plt.ylabel('Speed (km/h)')
        plt.title('Speed Profile')
        plt.grid(True)
        
        # Track curvature
        plt.subplot(2, 2, 2)
        plt.plot(self.track.distances, 1/np.maximum(self.track.curvatures, 1e-6))
        plt.xlabel('Distance (m)')
        plt.ylabel('Radius (m)')
        plt.title('Track Curvature')
        plt.grid(True)
        
        # Track layout
        plt.subplot(2, 2, (3, 4))
        self._plot_track_layout()
        
        plt.tight_layout()
        plt.show()
    
    def _plot_track_layout(self):
        """Plot 2D track layout from curvature data"""
        x, y = np.zeros(len(self.track.distances)), np.zeros(len(self.track.distances))
        heading = 0
        
        for i in range(1, len(self.track.distances)):
            ds = self.track.get_segment_length(i-1)
            curvature = self.track.curvatures[i-1]
            
            # Update position
            x[i] = x[i-1] + ds * np.cos(heading)
            y[i] = y[i-1] + ds * np.sin(heading)
            
            # Update heading
            heading += curvature * ds
        
        # Color by speed
        speeds = self.velocities * 3.6
        scatter = plt.scatter(x, y, c=speeds, cmap='RdYlGn', s=20)
        plt.colorbar(scatter, label='Speed (km/h)')
        plt.xlabel('X (m)')
        plt.ylabel('Y (m)')
        plt.title('Track Layout (colored by speed)')
        plt.axis('equal')
        plt.grid(True)
    
    def calculate_accelerations(self):
        """Calculate acceleration profile"""
        accelerations = np.zeros(len(self.velocities))
        for i in range(1, len(self.velocities)):
            dv = self.velocities[i] - self.velocities[i-1]
            ds = self.track.get_segment_length(i-1)
            dt = ds / max(self.velocities[i-1], 0.1)
            accelerations[i] = dv / dt
        return accelerations