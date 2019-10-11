cnt = 0

for i in range(1, 4):
    for j in range(1, 6):
        for k in range(1, 4):
            for l in range(1, 6):
                print('A: {}, {}, B: {}, {}'.format(i, j, k, l), end = '')
                
                if (i == j) != (k == l):
                    cnt += 1
                    print(', {}번째'.format(cnt))
                else:
                    print()