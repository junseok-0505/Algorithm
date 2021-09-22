import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deq = deque()

for i in range(n):
    editor = input().rstrip().split(' ')
    command = editor[0]

    if command == 'push':
        deq.append(editor[1])
    elif command == 'pop':
        if deq:
            a = deq.popleft()
            print(a)
        else:
            print(-1)
    elif command == 'size':
        print(len(deq))
    elif command == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif command == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)