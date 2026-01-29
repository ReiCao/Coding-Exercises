# Asking the inputs
Produto1, Quantidade1, Preço1 = input().split()
Produto2, Quantidade2, Preço2 = input().split()

# Numerize the Var's
Q1 = int(Quantidade1)
Q2 = int(Quantidade2)
P1 = float(Preço1)
P2 = float(Preço2)

# Equation
PreçoAPagar = (P1*Q1) + (P2*Q2)

# Print
print(f"VALOR A PAGAR: R$ {PreçoAPagar:.2F}")