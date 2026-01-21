import numpy as np
from track import Track
from vehicle import Vehicle
from tires import TireModel
from aero import AerodynamicsModel
from powertrain import PowertrainModel
from solver import LapTimeSolver
from analysis import LapAnalysis

def create_test_track():
    # Simple oval track: straight, corner, straight, corner
    segments = []
    
    # Straight section (500m)
    for i in range(50):
        segments.append((i * 10, 0.0))
    
    # Corner 1 (90 degree, R=50m)
    
    corner1_length = np.pi * 50 / 2  # Quarter circle
    for i in range(20):
        s = 500 + i * corner1_length / 20
        segments.append((s, 1/50))  # curvature = 1/radius
    
    # Straight section (500m)
    start_s = 500 + corner1_length
    for i in range(50):
        s = start_s + i * 10
        segments.append((s, 0.0))
    
    # Corner 2 (180 degree, R=50m)
    corner2_length = np.pi * 50
    start_s = 500 + corner1_length + 500
    for i in range(20):
        s = start_s + i * corner2_length / 20
        segments.append((s, 1/50))
    
    # Straight section (450m)
    start_s = 500 + corner1_length + 500 + corner2_length
    for i in range(40):
        s = start_s + i * 10
        segments.append((s, 0.0))

    # Corner 3 (90 degree, R=50m)
    start_s = 500 + corner1_length + 500 + corner2_length + 400
    corner3_length = np.pi * 50 / 2
    for i in range(20):
        s = start_s + i * corner3_length / 20
        segments.append((s, -1/50))

    # Straight section (450m)
    start_s = 500 + corner1_length + 500 + corner2_length + 400 + corner3_length
    for i in range(40):
        s = start_s + i * 10
        segments.append((s, 0.0))

    # Corner 4 (180 degree, R=50m)
    start_s = 500 + corner1_length + 500 + corner2_length + 400 + corner3_length + 400
    corner4_length = np.pi * 50
    for i in range(20):
        s = start_s + i * corner4_length / 20
        segments.append((s, 1/50))

    return Track(segments)

def main():
    print("Physics-Based Lap Time Simulator")
    print("=" * 40)
    
    # Create test track
    track = create_test_track()
    print(f"Track length: {track.total_length:.0f} m")
    
    # Vehicle setup
    vehicle = Vehicle(
        mass=600,           # kg
        wheel_radius=0.33,  # m
        drivetrain_efficiency=0.9,
        brake_force_max=12000  # N
    )
    
    # Tire model
    tire_model = TireModel(mu=1.4)  # Racing slicks
    
    # Aerodynamics (high downforce)
    aero_model = AerodynamicsModel(
        cl=3.0,           # High downforce
        cd=1.2,           # Drag coefficient
        frontal_area=1.8  # m²
    )
    
    # Powertrain
    powertrain_model = PowertrainModel(
        max_torque=450,   # Nm
        gear_ratio=4.0
    )
    
    # Solve lap time
    solver = LapTimeSolver(track, vehicle, tire_model, aero_model, powertrain_model)
    print("Solving optimal speed profile...")
    
    velocities = solver.solve()
    lap_time = solver.calculate_lap_time(velocities)
    
    # Analysis
    analysis = LapAnalysis(track, velocities, lap_time)
    analysis.print_summary()
    
    # Optional: Plot results
    analysis.plot_speed_profile()

if __name__ == "__main__":
    main()