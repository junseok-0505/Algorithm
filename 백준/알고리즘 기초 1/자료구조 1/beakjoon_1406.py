import sys
from collections import deque

input = sys.stdin.readline
deq = deque(input().rstrip())
deq2 = deque()
m = int(input())
for _ in range(m):
    editor = input().rstrip().split()
    command = editor[0]

    if command == 'L':
        if deq:
            deq2.append(deq.pop())
        else:
            continue

    elif command == 'D':
        if deq2:
            deq.append(deq2.pop())
        else:
            continue

    elif command == 'B':
        if deq:
            deq.pop()
        else:
            continue

    elif command == 'P':
        value = editor[1]
        deq.append(value)
        
deq2.reverse()
for i in deq+deq2:
    print(i, end='')