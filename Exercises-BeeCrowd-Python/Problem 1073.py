Target = int(input())

for i in range(0, Target+1, 2):
    if i == 0:
        continue
    print(f"{i}^2 = {i**2}")