# URI 1012
A,B,C = input().split()


A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

rectangled_triangle  = (0.5*(A * C))
area_of_circle = (pi * (C*C))
area_of_trapezium = ((.5) * (A + B) * C)
area_of_square = (B * B)
area_of_rectangle = (A * B)

print("TRIANGULO: %0.3f" %rectangled_triangle)
print("CIRCULO: %0.3f" %area_of_circle)
print("TRAPEZIO: %0.3f" %area_of_trapezium)
print("QUADRADO: %0.3f" %area_of_square)
print("RETANGULO: %0.3f" %area_of_rectangle)
