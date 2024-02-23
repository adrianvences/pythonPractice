
# You are given two interior angles (in degrees) of a triangle.

# Write a function to return the 3rd.

# Note: only positive integers will be tested.

def other_angle(a, b):
    missing_angle = 180 - a - b 
    return missing_angle