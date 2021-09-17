# 백준 18406

n = input()
check = []
for i in n:
    check.append(int(i))
    
length = int(len(check)/2)
    
if sum(check[:length]) == sum(check[length:]):
    print('LUCKY')
else:
    print('READY')
