# Asking The Input
X, Y, Z = input().split()


# Defining Variables
A = int(X)
B = int(Y)
C = int(Z)

#Equations
MaiorAB = (A+B+abs(A-B))/2
MaiorABC = (MaiorAB + C + abs(MaiorAB-C))/2

#Print
print(f"{MaiorABC:.0f} eh o maior")
