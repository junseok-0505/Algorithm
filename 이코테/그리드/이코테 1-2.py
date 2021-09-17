# 이코테 1-2.
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse=True)

count = 1
result = 0

a = m // k * k
result += data[0] * a
count += a
b = m - a
result += data[1] * b

print(result)
