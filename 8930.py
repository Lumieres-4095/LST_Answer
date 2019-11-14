rstIdx = 0

for a in range(2, 21):
    for b in range(2, 21):
        for c in range(2, 21):
            for d in range(2, 21):
                if a + b + c + d == 20 and \
                   d % a == 0 and \
                   d % b == 0 and \
                   d % c == 0:
                    rstIdx += 1
                    print([a, b, c, d], rstIdx)

print('\n총 경우의 수: {}'.format(rstIdx))