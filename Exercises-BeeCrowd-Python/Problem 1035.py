A, B, C, D = map(int, input().split())
E = A+B
F = C+D
if B > C and D > A and F > E and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")