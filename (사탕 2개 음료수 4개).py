''' 0 = 사탕 1
    1 = 사탕 2
    2 = 음료수 1
    3 = 음료수 2
    4 = 음료수 3
    5 = 음료수 4 '''

rstList = []

for A1 in range(6):
    for A2 in range(6):
        for B1 in range(6):
            for B2 in range(6):
                for C1 in range(6):
                    for C2 in range(6):
                        if A1 != A2 and A1 != B1 and A1 != B2 and A1 != C1 and A1 != C2 and \
                           A2 != B1 and A2 != B2 and A2 != C1 and A2 != C2 and \
                           B1 != B2 and B1 != C1 and B1 != C2 and \
                           B2 != C1 and B2 != C2 and \
                           C1 != C2:
                            if (A1 + A2 != 1) and (B1 + B2 != 1) and (C1 + C2 != 1):
                                if not [sorted([A1, A2]), sorted([B1, B2]), sorted([C1, C2])] in rstList:
                                    rstList.append([sorted([A1, A2]), sorted([B1, B2]), sorted([C1, C2])])

for i in range(len(rstList)):
    print('A: {}, B: {}, C: {}  {}번째'.format(rstList[i][0], rstList[i][1], rstList[i][2], i + 1))
