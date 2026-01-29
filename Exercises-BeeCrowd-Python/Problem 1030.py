CaseAmount = int(input())


for j in range(0, CaseAmount):
    NumPeople, Step = map(int, input().split())
    ListOfPeople = []
    first_iteration = True
    for i in range(0,NumPeople):
        ListOfPeople.append(i+1)

    while len(ListOfPeople) >= 2:
        if first_iteration:
            Killed_Pos = Step
            first_iteration = False
        else:
            Killed_Pos = Killed_Pos + Step - 1
        
        while Killed_Pos > len(ListOfPeople):
            Killed_Pos -= len(ListOfPeople)

        ListOfPeople.pop(Killed_Pos - 1)

    print(f"Case {j+1}: {str(ListOfPeople[0])}")