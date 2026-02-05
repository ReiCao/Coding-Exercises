Num1 = 0
Num2 = 2
while Num1 != Num2:
    Num1, Num2 = map(int, input().split())
    if Num1 < Num2:
        print("Crescente")
    elif Num1 > Num2:
        print("Decrescente")
