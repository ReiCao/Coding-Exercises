I = 1
J = 7
Bottom_J = 4
Top_J = 7

while I != 11 or J != 17:
    print(f"I={I} J={J}")
    J -= 1
    if J == Bottom_J:
        I += 2
        Top_J += 2
        Bottom_J += 2
        J = Top_J