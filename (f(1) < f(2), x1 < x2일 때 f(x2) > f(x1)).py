f = open("result2.txt", 'w')

cnt = 0

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            for l in range(1, 7):
                for m in range(1, 7):
                    for n in range(1, 7):
                        if i < j:
                            if k > l & l > m & m > n:
                                f.write('%d %d %d %d %d %d \n' % (i, j, k, l, m, n))
                                cnt += 1

f.write('\n{}'.format(cnt))
f.close()
