cnt = 0
 
for B1 in range(5):
    for B2 in range(5):
        for J in range(5):
            for S1 in range(5):
                for S2 in range(5):
                    if not B1 in (B2, J, S1, S2) and \
                       not B2 in (J, S1, S2) and \
                       not J in (S1, S2) and \
                       S1 != S2:
                        if B1 < J < B2 or B2 < J < B1:
                            printList = [i for i in range(5)]
                            cnt += 1

                            printList[B1] = 'B1'
                            printList[B2] = 'B2'
                            printList[J] = 'J'
                            printList[S1] = 'S1'
                            printList[S2] = 'S2'

                            print('( {}, {}, {}, {}, {} ), {}번째'.format(printList[0], 
                                                                        printList[1], 
                                                                        printList[2], 
                                                                        printList[3],
                                                                        printList[4], cnt))