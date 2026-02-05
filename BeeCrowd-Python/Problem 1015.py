import math

# Input
X1, Y1 = input().split()
X2, Y2 = input().split()

# Preparar Vars
x1 = float(X1)
y1 = float(Y1)
x2 = float(X2)
y2 = float(Y2)

# Equation

Distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{Distance:.4f}")