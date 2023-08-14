



import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real solutions
    
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    
    return math.ceil(x1), math.ceil(x2)

# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

solutions = solve_quadratic(a, b, c)
if solutions:
    print("Solutions:", solutions)
else:
    print("No real solutions")

