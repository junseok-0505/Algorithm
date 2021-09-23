import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deq = deque()
for _ in range(n):
    command = input().split()
    editor = command[0]

    if editor == 'push_front':
        deq.appendleft(command[1])
    elif editor == 'push_back':
        deq.append(command[1])
    elif editor == 'pop_front':
        if len(deq) != 0:
            a = deq.popleft()
            print(a)
        else:
            print(-1)
    elif editor == 'pop_back':
        if len(deq) != 0:
            a = deq.pop()
            print(a)
        else:
            print(-1)
    elif editor == 'size':
        print(len(deq))
    elif editor == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif editor == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif editor == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
