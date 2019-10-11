rstList114 = []
rstList123 = []
rstList222 = []
 
for el1 in range (6):
    for el2 in range (6):
        for el3 in range (6):
            for el4 in range (6):
                for el5 in range (6):
                    for el6 in range (6):
                        if (el1 != el2 and el1 != el3 and el1 != el4 and el1 != el5 and el1 != el6 and el2 != el3 and el2 != el4 and el2 != el5 and el2 != el6 and el3 != el4 and el3 != el5 and el3 != el6 and el4 != el5 and el4 != el6 and el5 != el6):
                            if not [[el1], [el2], sorted([el3, el4, el5, el6])] in rstList114 and not [[el2], [el1], sorted([el3, el4, el5, el6])] in rstList114:
                                rstList114.append([[el1], [el2], sorted([el3, el4, el5, el6])])

                            if not [[el1], sorted([el2, el3]), sorted([el4, el5, el6])] in rstList123:
                                rstList123.append([[el1], sorted([el2, el3]), sorted([el4, el5, el6])])

                            if not sorted([sorted([el1, el2]), sorted([el3, el4]), sorted([el5, el6])]) in rstList222:
                                rstList222.append(sorted([sorted([el1, el2]), sorted([el3, el4]), sorted([el5, el6])]))    

print('\n1 : 1 : 4')
for i in range(len(rstList114)):
    print('{}, {}번째'.format(rstList114[i], i + 1))
    
print('\n1 : 2 : 3')
for i in range(len(rstList123)):
    print('{}, {}번째'.format(rstList123[i], i + 1))

print('\n2 : 2 : 2')
for i in range(len(rstList222)):
    print('{}, {}번째'.format(rstList222[i], i + 1))