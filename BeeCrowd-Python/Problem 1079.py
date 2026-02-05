Case_Amount = int(input())

for i in range(Case_Amount):
    Num1, Num2, Num3 = map(float, input().split())
    print(f"{(Num1*2+Num2*3+Num3*5)/10:.1f}")