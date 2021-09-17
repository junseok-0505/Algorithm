# 이코테 Part3 1-2

s = input()
result = 0

for i in s:
    a = int(i)  
    if (a <= 1) or (result <= 1): result += a
        
    else: result *= a
        
print(result)
