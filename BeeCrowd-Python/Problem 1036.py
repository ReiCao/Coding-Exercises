import math

a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

Delta = b**2 - 4*a*c
if a <= 0 or Delta < 0:
    print("Impossivel calcular")
else:
    X1 = ((-1*b)+math.sqrt(Delta))/(2*a)
    X2 = ((-1*b)-math.sqrt(Delta))/(2*a)
    print(f"R1 = {X1:.5f}")
    print(f"R2 = {X2:.5f}")

