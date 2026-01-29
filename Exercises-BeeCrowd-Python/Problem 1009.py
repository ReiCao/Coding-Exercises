Name = input()
Salario = float(input())
Vendas = float(input())

SalarioComBonus = Salario + Vendas * 0.15

print(f"TOTAL = R$ {SalarioComBonus:.2F}")