import math

def circle_area(radius):
    return ((math.pi) * (radius ** 2))

area = circle_area(25)

print(f"The area of the circle with radius 25 is {area:.2f}")
