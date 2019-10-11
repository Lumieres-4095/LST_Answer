ans = 0

for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            for l in range(1, 6):
                for m in range(1, 6):
                    if set((i, j, k, l, m)) == set(range(1, 6)):
                        cnt = 0
                    
                        print('f(1) = {}, f(2) = {}, f(3) = {}, f(4) = {}, f(5) = {}'.format(i, j, k, l, m), end = ' ')

                        if i == 1:
                            cnt += 1
                        if j == 2:
                            cnt += 1
                        if k == 3:
                            cnt += 1
                        if l == 4:
                            cnt += 1
                        if m == 5:
                            cnt += 1

                        if cnt == 2:
                            print('O')
                            ans += 1
                        else:
                            print()

print('\n{}'.format(ans))