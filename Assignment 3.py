#Program that accepts the length of three sides of a triangle and determines the type of triangle is a right angle triangle or not using function
def is_right_triangle(a, b, c):
    # Sort the sides in ascending order
    sides = sorted([a, b, c])
    # Check if it's a right triangle using Pythagorean theorem
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9 

# Taking input from the user
side1, side2, side3 = map(float, input("Enter the lengths of three sides of the triangle separated by spaces: ").split())

# Check if it's a right triangle
if is_right_triangle(side1, side2, side3):
    print("The triangle is a right angle triangle.")
else:
    print("The triangle is not a right angle triangle.")

