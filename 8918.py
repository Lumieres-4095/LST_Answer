import sys
import math
from decimal import *

pointList = ['A', 'B', 'C', 'D']
rstCnt = 0

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                        start, end = 0, 2
                        verify = abs((i - start) * (j - i) * (k - j) * (l - k) * (m - l) * (end - m))
                        condition = math.log(verify, 3)

                        if verify != 0 and (verify == 1 or condition % 1 == 0):
                            rstCnt += 1
                            print([pointList[start], pointList[i], pointList[j], pointList[k], pointList[l], pointList[m], pointList[end]], rstCnt)

print('\n총 경우의 수: {}'.format(rstCnt))
