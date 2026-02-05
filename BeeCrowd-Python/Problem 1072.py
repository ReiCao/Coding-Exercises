Num_Amount = int(input())
In = 0
Out = 0
for i in range(Num_Amount):
    a = float(input())
    if a >= 10 and a <= 20:
        In += 1
    else:
        Out +=1
print(f"{In} in")
print(f"{Out} out")