cnt = 1

for i in range(-2, 3):
    for j in range(-2, 3):
        for k in range(-2, 3):
            for l in range(-2, 3):
                for m in range(-2, 3):
                    if i * j * k * l * m == 2:
                        print('f(1) = {}, f(2) = {}, f(3) = {}, f(4) = {}, f(5) = {}, {}번째'.format(i, j, k, l, m, cnt))
                        cnt += 1