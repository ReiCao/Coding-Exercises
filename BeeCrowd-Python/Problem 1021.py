# Input
Reais, Centavos = map(int, input().split("."))
# Preparar Var (n=nota nº=valor)
Notas = [100, 50, 20, 10, 5, 2]
Moedas = [100, 50, 25, 10, 5, 1]

# Equation
print("NOTAS:")
for Nota in Notas:
    print(f"{Reais//Nota} nota(s) de R$ {Nota}.00")
    Reais = Reais - ((Reais//Nota)*Nota)
    if Reais == 1:
        Centavos +=100
        Reais -= 1
print("MOEDAS:")
for Moeda in Moedas:
    print(f"{Centavos//Moeda} moeda(s) de R$ {Moeda/100:.2f}")
    Centavos = Centavos - ((Centavos//Moeda)*Moeda)
