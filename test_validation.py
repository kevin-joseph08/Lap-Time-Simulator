"""
Test validation functionality
"""
from track import Track
from vehicle import Vehicle
from tires import TireModel
from aero import AerodynamicsModel
from powertrain import PowertrainModel
from validation import ValidationError

def test_validation():
    print("Testing Input Validation\n" + "="*50)
    
    # Test Track validation
    print("\n1. Track Validation:")
    try:
        Track([(-10, 0), (100, 0)])
        print("  FAIL: Should have failed: negative distance")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    try:
        Track([(0, 0), (100, 2.0)])
        print("  FAIL: Should have failed: excessive curvature")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    try:
        Track([(100, 0), (50, 0)])
        print("  FAIL: Should have failed: non-increasing distances")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    # Test Vehicle validation
    print("\n2. Vehicle Validation:")
    try:
        Vehicle(mass=-100)
        print("  FAIL: Should have failed: negative mass")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    try:
        Vehicle(mass=600, drivetrain_efficiency=1.5)
        print("  FAIL: Should have failed: efficiency > 1")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    try:
        Vehicle(mass=15000)
        print("  FAIL: Should have failed: unrealistic mass")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    # Test TireModel validation
    print("\n3. Tire Model Validation:")
    try:
        TireModel(mu=0)
        print("  FAIL: Should have failed: zero friction")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    try:
        TireModel(mu=5.0)
        print("  FAIL: Should have failed: unrealistic friction")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    # Test AerodynamicsModel validation
    print("\n4. Aerodynamics Model Validation:")
    try:
        AerodynamicsModel(cd=-1)
        print("  FAIL: Should have failed: negative drag")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    try:
        AerodynamicsModel(cl=15)
        print("  FAIL: Should have failed: excessive lift coefficient")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    # Test PowertrainModel validation
    print("\n5. Powertrain Model Validation:")
    try:
        PowertrainModel(max_torque=0)
        print("  FAIL: Should have failed: zero torque")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    try:
        PowertrainModel(gear_ratio=50)
        print("  FAIL: Should have failed: excessive gear ratio")
    except ValidationError as e:
        print(f"  PASS: Caught: {e}")
    
    # Test valid configuration
    print("\n6. Valid Configuration:")
    try:
        track = Track([(0, 0), (100, 0.01), (200, 0)])
        vehicle = Vehicle(mass=600)
        tire = TireModel(mu=1.4)
        aero = AerodynamicsModel(cl=3.0, cd=1.2)
        powertrain = PowertrainModel(max_torque=450)
        print("  PASS: All components created successfully")
    except ValidationError as e:
        print(f"  FAIL: Unexpected error: {e}")
    
    print("\n" + "="*50)
    print("Validation tests complete!")

if __name__ == "__main__":
    test_validation()
