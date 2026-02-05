# Input
Seconds = int(input())

# Preparar Var
Minutes = 0
Hours = 0

# Equation
while Seconds > 59:
    Minutes += 1
    Seconds -= 60
    if Minutes > 60:
        Hours += 1
        Minutes -= 60

# print
print(f"{Hours}:{Minutes}:{Seconds}")