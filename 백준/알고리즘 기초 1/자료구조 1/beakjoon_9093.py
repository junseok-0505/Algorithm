# 백준 10828
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    text = input().rstrip().split(' ')
    for i in text:
        print(i[len(i)::-1], end=' ')