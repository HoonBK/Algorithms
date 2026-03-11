import sys

n = int(sys.stdin.readline())

p = list(map(int,sys.stdin.readline().split()))

p.sort()

result=0
for i in range(1,n+1):
    result+=p.pop()*i
print(result)