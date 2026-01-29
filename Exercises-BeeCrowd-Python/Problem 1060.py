Num_List = []
Positive_Num = 0
for i in range(0, 6):
    a = float(input())
    Num_List.append(a)

for Num in Num_List:  
    if Num > 0:
        Positive_Num += 1
    else:
        continue

print(f"{Positive_Num} valores positivos")