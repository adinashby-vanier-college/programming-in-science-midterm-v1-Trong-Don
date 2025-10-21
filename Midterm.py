import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * (radius ** 2)
    
    return round(area,2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    triangle = ""

    if n < 4:
        return 'The triangle height should be at least 4.'

    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i or i == n - 1:
                triangle += "*"
            else:
                triangle += " "

        triangle += "\n"

    return triangle.rstrip()

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    pyramid = ""

    if n < 3:
        return "The pyramid height should be at least 3."
    
    for i in range(n, 0, -1):
        spacing = (n - i) * " "
        star = (2 * i - 1) * "*"
        pyramid += spacing + star + "\n"

    return pyramid.rstrip()

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()