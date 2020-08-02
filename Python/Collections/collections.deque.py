from collections import *

N = int(input())
d = deque()

for i in range(N):
    args = input().strip().split()
    if args[0] == 'append':
        d.append(args[1])
    elif args[0] == 'pop':
        d.pop()
    elif args[0] == 'popleft':
        d.popleft()
    elif args[0] == 'appendleft':
        d.appendleft(args[1])

print(' '.join(d))
