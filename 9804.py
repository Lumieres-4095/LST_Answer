setBElements = (1, 2, 3, 4, 8, 9)
setA, setB = [], []

for i in range(1, 8):
    for j in range(1, 8):
        if i != j:
            setA.append([i, j])
            print('setA: [ {}, {} ] {}'.format(i, j, len(setA)))

for a in setBElements:
    for b in setBElements:
        if i != j:
            setB.append([a, b])
            print('setA: [ {}, {} ] {}'.format(a, b, len(setB)))

print('n(A) = {}, n(B) = {}'.format(len(setA), len(setB)))
print('n(A∪ B) = {}'.format(len(setA + setB)))