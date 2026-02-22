# Input Validation & Error Handling

## Overview
Added comprehensive input validation to all simulator components with clear, actionable error messages.

## Files Added
- `validation.py` - Core validation utilities and custom ValidationError exception

## Files Modified
- `track.py` - Track data validation
- `vehicle.py` - Vehicle parameter validation
- `tires.py` - Tire model validation
- `aero.py` - Aerodynamics parameter validation
- `powertrain.py` - Powertrain parameter validation

## Validation Rules

### Track
- At least 2 segments required
- All distances must be non-negative
- Distances must be strictly increasing
- Curvature magnitude <= 1.0 /m (minimum 1m radius)

### Vehicle
- Mass: positive, <= 10000 kg
- Wheel radius: positive, <= 1.0 m
- Drivetrain efficiency: 0.1 to 1.0
- Brake force: positive

### Tire Model
- Coefficient of friction: positive, <= 2.5

### Aerodynamics
- Drag coefficient: positive, <= 5
- Lift coefficient: |cl| <= 10
- Frontal area: positive, <= 10 m^2
- Air density: positive

### Powertrain
- Max torque: positive, <= 2000 Nm
- Gear ratio: positive, <= 20

## Usage

```python
from validation import ValidationError

try:
    vehicle = Vehicle(mass=-100)  # Invalid
except ValidationError as e:
    print(f"Error: {e}")
    # Output: Error: Vehicle mass must be positive, got -100
```

## Testing
Run validation tests:
```bash
python test_validation.py
```

All tests pass with clear error messages for invalid inputs.
