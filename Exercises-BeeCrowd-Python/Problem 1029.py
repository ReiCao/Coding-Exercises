CaseAmount = int(input())

def fib(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

for i in range(0,CaseAmount):
    Fib_Num = int(input())
    Answer = fib(Fib_Num)
    FibNum1 = Fib_Num+1
    calls = 2*fib(FibNum1) - 2
    if Fib_Num == 0:
        Result = 0
        calls = 0
        print(f"fib({Fib_Num})= {calls} calls = {Result}")
    else:
        print(f"fib({Fib_Num}) = {calls} calls = {Answer}")