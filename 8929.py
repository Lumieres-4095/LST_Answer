subjList = ('물리 I', '화학 I', '생물 I', '지구과학 I', '물리 II', '화학 II', '생물 II', '지구과학 II')
ansList, tempList = [], []

for subject1 in range(8):
    for subject2 in range(8):
        for subject3 in range(8):
            if not subject1 in (subject2, subject3) and \
               subject2 != subject3:
                if subject1 <= 3 or subject2 <= 3 or subject3 <= 3:
                    tempList.append(sorted([subjList[subject1], subjList[subject2], subjList[subject3]]))

for a in tempList:
    if not a in ansList:
        ansList.append(a)

for j in range(len(ansList)):
    print(ansList[j], ', {} 번째'.format(j + 1))

print('총 경우의 수: {}'.format(len(ansList)))
