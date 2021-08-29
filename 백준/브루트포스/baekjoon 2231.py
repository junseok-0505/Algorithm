n = int(input())

if n == 1:
    print(0)
    
else:
    for i in range(0, n):
        result = i + sum(map(int, str(i)))
        
        if result == n:
            print(i)
            break
        elif i+1 == n:
            print(0)
            