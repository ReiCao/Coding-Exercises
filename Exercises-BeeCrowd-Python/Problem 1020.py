# Input
Days = int(input())

# Preparar Var
Months = 0
Years = 0

# Equation
while Days > 364:
    Years += 1
    Days -= 365
while Days > 29:
    Months += 1
    Days -= 30

# print
print(f"{Years} ano(s)")
print(f"{Months} mes(es)")
print(f"{Days} dia(s)")