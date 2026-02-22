class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

def validate_positive(value, name):
    if value <= 0:
        raise ValidationError(f"{name} must be positive, got {value}")

def validate_non_negative(value, name):
    if value < 0:
        raise ValidationError(f"{name} must be non-negative, got {value}")

def validate_range(value, name, min_val, max_val):
    if not min_val <= value <= max_val:
        raise ValidationError(f"{name} must be between {min_val} and {max_val}, got {value}")
