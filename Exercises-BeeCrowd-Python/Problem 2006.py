T = int(input())

Respostas = input()

Lista = Respostas.split()

A = int(Lista[0])
B = int(Lista[1])
C = int(Lista[2])
D = int(Lista[3])
E = int(Lista[4])

Answers = [A,B,C,D,E]

Total = 0

for i in Answers:
    if i == T:
        Total += 1

print(Total)
