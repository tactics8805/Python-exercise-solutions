import math
r = abs(float(input("Enter the value of the radius of the cylinder: ")))
h = abs(float(input("Enter the value of the height of the cylinder: ")))
def cylinder_volume(r: float, h: float) -> float:
    """Calculate the volume of a cylinder.

    Args:
        r (float): The radius of the cylinder's base. Volume is always positive so we take absolute value.
        h (float): The height of the cylinder. Volume is always positive so we take absolute value.

    Returns:
        float: The volume of the cylinder.
    """
    return math.pi * r**2 * h
print(f"The volume of the cylinder is: {cylinder_volume(r, h)}")
# Test cases
assert cylinder_volume(3,5) == math.pi * 3**2 * 5
assert cylinder_volume(0,10) == 0
assert cylinder_volume(2.5,4) == math.pi * 2.5**2 * 4