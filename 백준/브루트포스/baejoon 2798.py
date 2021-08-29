from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
result = []

for i in combinations(card, 3):
    if sum(i) <= m:
        result.append(sum(i))
        
print(max(result))