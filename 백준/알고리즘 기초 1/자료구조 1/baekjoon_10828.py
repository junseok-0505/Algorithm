# 백준 10828
import sys
input = sys.stdin.readline
number = int(input())
def push(data):
    stack.append(data)
    
def pop():
    if len(stack) != 0:
        data = stack[-1]
        del stack[-1]
        return print(data)
    else:
        return print(-1)

def size():
    return print(len(stack))

def empty():
    if len(stack) == 0:
        return print(1)
    else:
        return print(0)
    
def top():
    if len(stack) == 0:
        return print(-1)
    else:
        return print(stack[-1])


stack = []
for _ in range(number):
    input_split = input().split()
    
    order = input_split[0]
    
    if order == 'push':
        push(int(input_split[1]))
    elif order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'top':
        top()
