# Input
QuantoTem = int(input())

Dinheiro = QuantoTem
# Preparar Var (n=nota nº=valor)
N100 = 0
N50 = 0
N20 = 0
N10 = 0
N5 = 0
N2 = 0
N1 = 0

# Equation
while Dinheiro > 0:
    while Dinheiro >=100:
        Dinheiro -=100
        N100 +=1
    while Dinheiro >= 50:
        Dinheiro -=50
        N50 +=1
    while Dinheiro >= 20:
        Dinheiro -=20
        N20 +=1
    while Dinheiro >= 10:
        Dinheiro -=10
        N10 +=1
    while Dinheiro >= 5:
        Dinheiro -=5
        N5 +=1
    while Dinheiro >= 2:
        Dinheiro -=2
        N2 +=1
    while Dinheiro >= 1:
        Dinheiro -=1
        N1 +=1

print(QuantoTem)
print(f"{N100} nota(s) de R$ 100,00")
print(f"{N50} nota(s) de R$ 50,00")
print(f"{N20} nota(s) de R$ 20,00")
print(f"{N10} nota(s) de R$ 10,00")
print(f"{N5} nota(s) de R$ 5,00")
print(f"{N2} nota(s) de R$ 2,00")
print(f"{N1} nota(s) de R$ 1,00")