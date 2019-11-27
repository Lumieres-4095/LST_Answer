cnt = 0

for r1 in range(8):
    for r2 in range(8):
        for r3 in range(8):
            for b1 in range(8):
                for b2 in range(8):
                    for b3 in range(8):
                        for y1 in range(8):
                            for y2 in range(8):
                                if set((r1, r2, r3, b1, b2, b3, y1, y2)) == set(range(8)) and \
                                  (abs(r1 - r2) == 1 and abs(r2 - r3) != 1 and abs(r3 - r1) != 1 or \
                                   abs(r1 - r2) != 1 and abs(r2 - r3) == 1 and abs(r3 - r1) != 1 or \
                                   abs(r1 - r2) != 1 and abs(r2 - r3) != 1 and abs(r3 - r1) == 1):
                                    arr = [0 for _ in range(8)]
                                    
                                    arr[r1], arr[r2], arr[r3] = 'R', 'R', 'R'
                                    arr[b1], arr[b2], arr[b3] = 'B', 'B', 'B'
                                    arr[y1], arr[y2] = 'Y', 'Y'

                                    cnt += 1
                                    print('{}, {}번째'.format(arr, cnt))

print('총 경우의 수: {}'.format(cnt)) # 150