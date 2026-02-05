Codigo, Quantidade = map(int, input().split())

Preço = 0
if Codigo == 1:
    Preço = 4 * Quantidade
elif Codigo == 2:
    Preço = 4.5 * Quantidade
elif Codigo == 3:
    Preço = 5 * Quantidade
elif Codigo == 4:
    Preço = 2 * Quantidade
elif Codigo == 5:
    Preço = 1.5 * Quantidade


print(f"Total: R$ {Preço:.2f}")
