# validation.py

def validate_roll_number(roll_number):
    if isinstance(roll_number, int) and roll_number > 0:
        return True
    return False

def validate_cgpa(cgpa):
    if 0.0 <= cgpa <= 10.0:
        return True
    return False
