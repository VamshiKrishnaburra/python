def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
    
    
    if a == b == c:
        t_type = "Equilateral"
    elif a == b or b == c or a == c:
        t_type = "Isosceles"
    else:
        t_type = "Scalene"
    
    sides = sorted([a, b, c])  
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return f"{t_type} and Right-angled"
    else:
        return t_type

print(triangle_type(3, 4, 5))   
print(triangle_type(5, 5, 5))  
print(triangle_type(5, 5, 8))  
print(triangle_type(2, 3, 6))   
