sumCnt, rstCnt, rstList = 0, 0, []

for seat1 in range(1, 7):
    for seat2 in range(1, 7):
        for seat3 in range(1, 7):
            for seat4 in range(1, 7):
                for seat5 in range(1, 7):
                    for seat6 in range(1, 7):
                        if not seat1 in (seat2, seat3, seat4, seat5, seat6) and \
                           not seat2 in (seat3, seat4, seat5, seat6) and\
                           not seat3 in (seat4, seat5, seat6) and \
                           not seat4 in (seat5, seat6) and \
                           seat5 != seat6:

                            if 1 in (seat1, seat3, seat4, seat6) and \
                               2 in (seat1, seat3, seat4, seat6):
                                rstList.append([seat1, seat2, seat3, seat4, seat5, seat6])

for i in range(len(rstList)):
    if rstList[i][::-1] in rstList:
        rstList[i] = ['Overrided List']

while True:
    try:
        rstList.remove(['Overrided List'])
    except ValueError:
        break

for seat1 in range(1, 7):
    for seat2 in range(1, 7):
        for seat3 in range(1, 7):
            for seat4 in range(1, 7):
                for seat5 in range(1, 7):
                    for seat6 in range(1, 7):
                        if not seat1 in (seat2, seat3, seat4, seat5, seat6) and \
                           not seat2 in (seat3, seat4, seat5, seat6) and\
                           not seat3 in (seat4, seat5, seat6) and \
                           not seat4 in (seat5, seat6) and \
                           seat5 != seat6:
                            sumCnt += 1
                            print(sumCnt, [seat1, seat2, seat3, seat4, seat5, seat6], end = '')

                            if [seat1, seat2, seat3, seat4, seat5, seat6] in rstList:
                                rstCnt += 1
                                print(', {}번째'.format(rstCnt))
                            else:
                                print()
                               
print('총 경우의 수: {}'.format(rstCnt))