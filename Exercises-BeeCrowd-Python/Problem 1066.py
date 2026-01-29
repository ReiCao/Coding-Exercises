Num_List = []
Even_Num = 0
Odd_Num = 0
Positive_Num = 0
Negative_Num = 0
for i in range(0, 5):
    a = float(input())
    Num_List.append(a)

for Num in Num_List:  
    if Num % 2 == 0 or Num == 0:
        Even_Num += 1
    elif Num % 2 != 0:
        Odd_Num += 1
    
    if Num < 0:
        Negative_Num +=1
    elif Num > 0:
        Positive_Num += 1

print(f"{Even_Num} valor(es) par(es)")
print(f"{Odd_Num} valor(es) impar(es)")
print(f"{Positive_Num} valor(es) positivo(s)")
print(f"{Negative_Num} valor(es) negativo(s)")