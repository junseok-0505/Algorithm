# 백준 9012
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    result = 0
    vps = input().rstrip()
    for i in vps:
        if i == '(':
           result += 1
        else:
            result -= 1
        if result == -1:
            answer = 'NO'
            break
    if result != 0:
        answer = 'NO'
    else:
        answer = 'YES'
    print(answer)