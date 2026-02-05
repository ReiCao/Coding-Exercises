from fractions import Fraction

Casos = int(input())
ListaDeCasos = []

def validate(s):
    values = float(s)
    if values % 2 == 0:
        return False
    elif values == 1:
        return False
    else:
        return True

for x in range(0, Casos):
    Caso = input()
    ListaDeCasos.append(Caso)

for Case in ListaDeCasos:
    n1, O1, d1, OP, n2, O2, d2 = Case.split()
    N1 = int(n1)
    D1 = int(d1)
    N2 = int(n2)
    D2 = int(d2)
    if OP == "+": 
        R1 = N1*D2 + N2*D1 
        R2 = D1*D2
        R3 = Fraction(R1, R2)
        if validate(R3):
            print(f"{R1}/{R2} = {R3}")
        else:
            print(f"{R1}/{R2} = {R3}/1")
    if OP == "-": 
        R1 = N1*D2 - N2*D1
        R2 = D1*D2
        R3 = Fraction(R1, R2)
        if validate(R3):
            print(f"{R1}/{R2} = {R3}")
        else:
            print(f"{R1}/{R2} = {R3}/1")
    if OP == "*": 
        R1 = N1*N2
        R2 = D1*D2
        R3 = Fraction(R1, R2)
        if validate(R3):
            print(f"{R1}/{R2} = {R3}")
        else:
            print(f"{R1}/{R2} = {R3}/1")
    if OP == "/": 
        R1 = N1*D2
        R2 = N2*D1
        R3 = Fraction(R1, R2)
        if validate(R3):
            print(f"{R1}/{R2} = {R3}")
        else:
            print(f"{R1}/{R2} = {R3}/1")