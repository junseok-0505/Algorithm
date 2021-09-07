# 이코테 Part3 1-5

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
count = 0

for i in range(n):
    for j in range(i, n):
        if data[i] != data[j]:
            count+=1
            
print(count)