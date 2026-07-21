def is_number(value):
    """Check if the input can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False