setBElements = (1, 2, 3, 4, 8, 9)
setA, setB = [], []

for i in range(1, 8):
    for j in range(1, 8):
        if i != j:
            setA.append(10 * i + j)

for k in setBElements:
    for l in setBElements:
        if k != l:
            setB.append(10 * k + l)

'''
newSet = [setA, setB]
newestSet = []

for _ in range(2):
    for __ in range(len(newSet[_])):
        if not newSet[_][__] in newestSet:
            newestSet.append(newSet[_][__])
'''

print('n(A) = {}, n(B) = {}'.format(len(setA), len(setB)))
print('n(A∪B) = {}'.format(len(set(setA + setB))))
