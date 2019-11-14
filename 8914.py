import itertools # itertools.product(A, B) is as same as product set of A, B.

index, answerIndex = 0, 0
rstList = []

innerColor = ('R', 'B', 'Y', 'G') # Red, Blue, Yellow, Green
outerColor = ('A', 'B', 'C', 'D') # Orange, Purple, Pink, Light green

for inner1, outer1 in itertools.product(innerColor, outerColor):
    for inner2, outer2 in itertools.product(innerColor, outerColor):
        for inner3, outer3 in itertools.product(innerColor, outerColor):
            for inner4, outer4 in itertools.product(innerColor, outerColor):
                if set((inner1, inner2, inner3, inner4)) == set(innerColor) and \
                   set((outer1, outer2, outer3, outer4)) == set(outerColor):
                    answerIndex += 1
                    rstList.append([inner1, inner2, inner3, inner4, outer1, outer2, outer3, outer4])

for i in range(len(rstList)):
    if rstList[i][::-1] in rstList:
        rstList[i] = ['Overrided List']

while True:
    try:
        rstList.remove(['Overrided List'])
    except ValueError:
        break

for inner1, outer1 in itertools.product(innerColor, outerColor):
    for inner2, outer2 in itertools.product(innerColor, outerColor):
        for inner3, outer3 in itertools.product(innerColor, outerColor):
            for inner4, outer4 in itertools.product(innerColor, outerColor):
                if [inner1, inner2, inner3, inner4, outer1, outer2, outer3, outer4] in rstList:
                    answerIndex += 1
                    print(', {}번째'.format(answerIndex))
                else:
                    print()

print('총 경우의 수: {}'.format(answerIndex))