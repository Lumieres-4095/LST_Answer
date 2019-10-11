cnt = 0

for i in range(8):
    for j in range(6):
        for k in range(4):
            print('{}{}{}'.format(i, j, k), end = '')

            if i != j != k:
                cnt += 1
                print(', {}번째'.format(cnt))
            else:
                print()