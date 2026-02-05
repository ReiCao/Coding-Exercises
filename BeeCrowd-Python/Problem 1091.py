Input_Ended = False

while Input_Ended == False:
    Query_Amount = int(input())

    if Query_Amount == 0:
        break

    Div1, Div2 = map(int, input().split())

    for i in range(0, Query_Amount):
        Cord1, Cord2 = map(int, input().split())
        if Cord1 == Div1 or Cord2 == Div2:
            print("divisa")
        elif Cord1 > Div1 and Cord2 > Div2:
            print("NE")
        elif Cord1 < Div1 and Cord2 < Div2:
            print("SO")
        elif Cord1 < Div1 and Cord2 > Div2:
            print("NO")
        elif Cord1 > Div1 and Cord2 < Div2:
            print("SE")