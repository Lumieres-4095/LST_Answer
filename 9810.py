cnt = 0
eleArr = (1, 1, 2, 2, 3, 3, 4, 4, 5, 5)
sameArr = []

def IsCase(result)

for i in range(10):
    for j in range(10):
        print('({}, {})'.format(eleArr[i], eleArr[j]), end = '')
        
        if (eleArr[i] + eleArr[j]) % 2 == 0:            
            if eleArr[i] == eleArr[j]:         
                if not (eleArr[i], eleArr[j]) in sameArr:
                    cnt += 1
                    print(', {}번째'.format(cnt))
                    sameArr.append((eleArr[i], eleArr[j]))
                else:
                    print()
            else:
                cnt += 1
                print(', {}번째'.format(cnt))
        else:
            print()