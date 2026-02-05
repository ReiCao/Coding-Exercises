CaseAmount = int(input())

def mdc(x,y):
    while(y):
        x,y=y,x%y
    return x

for x in range(0, CaseAmount):
    P1, P2 = map(int, input().split())
    print(mdc(P1,P2))