I = 1
J = 7

while I != 9 or J != 5:
    print(f"I={I} J={J}")
    J -= 1
    if J == 4:
        I += 2
    if J < 5:
        J = 7
print(f"I={I} J={J}")