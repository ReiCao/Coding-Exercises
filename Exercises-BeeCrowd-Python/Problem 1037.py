Numero = float(input())

if Numero >= 0 and Numero <= 25:
    print("Intervalo [0,25]")
elif Numero > 25 and Numero <= 50:
    print("Intervalo (25,50]")
elif Numero > 50 and Numero <= 75:
    print("Intervalo (50,75]")
elif Numero > 75 and Numero <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")