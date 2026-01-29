Case_Amount = int(input())
Result = 0
for i in range(0,Case_Amount):
    a, b = map(int, input().split())
    if a > b:
        temp = b
        b = a
        a = temp

    for i in range(a+1,b):
        if i % 2 != 0:
            Result += i
    print(Result)
    Result = 0