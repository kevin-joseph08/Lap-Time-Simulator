import numpy as np
from track import Track
from vehicle import Vehicle
from tires import TireModel
from aero import AerodynamicsModel
from powertrain import PowertrainModel
from solver import LapTimeSolver

def test_straight_line():
    """Test acceleration on a straight line"""
    print("Testing straight line acceleration...")
    
    # Create straight track (1000m)
    segments = [(i * 10, 0.0) for i in range(100)]
    track = Track(segments)
    
    # Simple vehicle
    vehicle = Vehicle(mass=1000, wheel_radius=0.3)
    tire_model = TireModel(mu=1.0)
    aero_model = AerodynamicsModel(cl=0, cd=0.3, frontal_area=2.0)
    powertrain_model = PowertrainModel(max_torque=300, gear_ratio=3.0)
    
    solver = LapTimeSolver(track, vehicle, tire_model, aero_model, powertrain_model)
    velocities = solver.solve()
    lap_time = solver.calculate_lap_time(velocities)
    
    print(f"Final speed: {velocities[-1] * 3.6:.1f} km/h")
    print(f"Time: {lap_time:.1f} seconds")
    print()

def test_constant_radius():
    """Test cornering at constant radius"""
    print("Testing constant radius corner...")
    
    # Circular track (R=100m)
    radius = 100
    circumference = 2 * np.pi * radius
    n_segments = 50
    ds = circumference / n_segments
    
    segments = []
    for i in range(n_segments):
        s = i * ds
        segments.append((s, 1/radius))  # constant curvature
    
    track = Track(segments)
    
    vehicle = Vehicle(mass=800)
    tire_model = TireModel(mu=1.2)
    aero_model = AerodynamicsModel(cl=2.0, cd=1.0, frontal_area=1.8)
    powertrain_model = PowertrainModel(max_torque=400, gear_ratio=4.0)
    
    solver = LapTimeSolver(track, vehicle, tire_model, aero_model, powertrain_model)
    velocities = solver.solve()
    lap_time = solver.calculate_lap_time(velocities)
    
    # Theoretical max speed for constant radius
    normal_force = vehicle.mass * 9.81  # No aero at low speed
    v_theoretical = np.sqrt(tire_model.mu * normal_force * radius / vehicle.mass)
    
    print(f"Corner speed: {np.mean(velocities) * 3.6:.1f} km/h")
    print(f"Theoretical max: {v_theoretical * 3.6:.1f} km/h")
    print(f"Lap time: {lap_time:.1f} seconds")
    print()

if __name__ == "__main__":
    test_straight_line()
    test_constant_radius()