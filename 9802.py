cnt = 0

for f1 in range(1, 6):
    for f2 in range(1, 6):
        for f3 in range(1, 6):
            for f4 in range(1, 6):
                for f5 in range(1, 6):
                    print('f(1) = {}, f(2) = {}, f(3) = {}, f(4) = {}, f(5) = {}'.format(f1, f2, f3, f4, f5), end = '')

                    if (1 + f1) % 2 != 0 and \
                       (2 + f2) % 2 != 0 and \
                       (3 + f3) % 2 != 0 and \
                       (4 + f4) % 2 != 0 and \
                       (5 + f5) % 2 != 0:
                        cnt += 1
                        print(', {}번째'.format(cnt))
                    else:
                        print('')