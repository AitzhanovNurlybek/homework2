def triangle_type(x, y, z):
    if x == y and y == z:
            return "Equilateral triangle"
    elif x == y or y == z or x == z:
            return "Isosceles triangle"
    else:
            return "Scalene triangle"
    
        

print("Input lengths of the triangle sides:")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

print(triangle_type(x, y, z))