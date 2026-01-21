# Physics-Based Lap Time Simulator

A physics-based lap time simulator that computes the minimum achievable lap time for a vehicle around a given track, enforcing realistic physical constraints.

## Features

- Physics-based speed profile calculation
- Tire friction limits (friction circle model)
- Aerodynamic downforce and drag
- Powertrain acceleration limits
- Braking constraints
- Forward/backward pass optimization

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the simulator:
```bash
python main.py
```

3. Run physics tests:
```bash
python test_physics.py
```

## Usage

### Basic Example

```python
from track import Track
from vehicle import Vehicle
from tires import TireModel
from aero import AerodynamicsModel
from powertrain import PowertrainModel
from solver import LapTimeSolver
from analysis import LapAnalysis

# Load track from CSV
track = Track.from_csv('sample_track.csv')

# Configure vehicle
vehicle = Vehicle(mass=600, wheel_radius=0.33)
tire_model = TireModel(mu=1.4)
aero_model = AerodynamicsModel(cl=3.0, cd=1.2, frontal_area=1.8)
powertrain_model = PowertrainModel(max_torque=450, gear_ratio=4.0)

# Solve
solver = LapTimeSolver(track, vehicle, tire_model, aero_model, powertrain_model)
velocities = solver.solve()
lap_time = solver.calculate_lap_time(velocities)

# Analyze results
analysis = LapAnalysis(track, velocities, lap_time)
analysis.print_summary()
analysis.plot_speed_profile()
```

### Track Format

CSV format with columns:
- `s`: cumulative distance (m)
- `curvature`: 1/radius (1/m), positive for left turns

Example:
```csv
s,curvature
0,0.0
100,0.0
200,0.02
300,0.02
400,0.0
```

## Model Parameters

### Vehicle
- `mass`: vehicle mass (kg)
- `wheel_radius`: wheel radius (m)
- `drivetrain_efficiency`: efficiency factor
- `brake_force_max`: maximum brake force (N)

### Tires
- `mu`: coefficient of friction

### Aerodynamics
- `cl`: lift coefficient (negative for downforce)
- `cd`: drag coefficient
- `frontal_area`: frontal area (m²)
- `air_density`: air density (kg/m³)

### Powertrain
- `max_torque`: maximum engine torque (Nm)
- `gear_ratio`: gear ratio

## Physics Model

The simulator formulas:

1. **Friction Circle**: √(Fx² + Fy²) ≤ μFz
2. **Cornering Speed**: v ≤ √(μFzr/m)
3. **Acceleration**: a = (Fengine - Fdrag)/m
4. **Braking**: a ≤ μFz/m

## Output

- Total lap time
- Speed profile vs distance
- Maximum and average speeds
- Optional plots (requires matplotlib)

## Validation

The simulator includes physics validation tests:
- Straight line acceleration
- Constant radius cornering
- Comparison with theoretical limits

## Limitations

- Simplified tire model (constant μ)
- No elevation changes
- Single gear ratio
- No transient dynamics
- Assumes optimal driver behavior

## Extensions

Future enhancements could include:
- Variable tire grip
- Multi-gear transmission
- Track elevation
- Tire temperature effects
- Energy recovery systems