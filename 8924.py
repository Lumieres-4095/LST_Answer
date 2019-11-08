cnt, rstCnt = 0, 0

for i in range(1, 6): # 첫 번째 공
    for j in range(1, 6): # 두 번째 공
        for k in range(1, 6): # 세 번째 공
            for l in range(1, 6): # 네 번째 공
                cnt += 1
                print(cnt, [i, j, k, l], end = '')

                if i % 2 == 0 or \
                   j % 2 == 0 or \
                   k % 2 == 0 or \
                   l % 2 == 0:
                    rstCnt += 1
                    print(', {} 번째'.format(rstCnt))
                else:
                    print()

print('\n총 경우의 수: ', rstCnt, ' / ', cnt)
