Num_List = []
Even_Num = 0
for i in range(0, 5):
    a = float(input())
    Num_List.append(a)

for Num in Num_List:  
    if Num % 2 == 0:
        Even_Num += 1
    else:
        continue

print(f"{Even_Num} valores pares")