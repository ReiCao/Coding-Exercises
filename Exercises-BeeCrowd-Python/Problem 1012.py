# Asking The Input
X, Y, Z = input().split()


# Defining Variables
A = float(X)
B = float(Y)
C = float(Z)
Pi = 3.14159

#Equations
Triangulo = (A*C)/2
Circulo = Pi*(C**2)
Trapezio = (A+B)*(C/2)
Quadrado = (B*B)
Retangulo = (A*B)

#Print
print(f"TRIANGULO: {Triangulo:.3f}")
print(f"CIRCULO: {Circulo:.3f}")
print(f"TRAPEZIO: {Trapezio:.3f}")
print(f"QUADRADO: {Quadrado:.3f}")
print(f"RETANGULO: {Retangulo:.3f}")