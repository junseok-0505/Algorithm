# 이코테 1-4.

n, m = map(int, input().split())
result = 0

while True:
    if n % m != 0:
        n -= 1
        result += 1
    else:
        n = n / m
        result += 1
    if n == 1:
        break
    
print(result)
