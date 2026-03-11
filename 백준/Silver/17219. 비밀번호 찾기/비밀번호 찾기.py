import sys

n,m = map(int, sys.stdin.readline().split())

dic = dict()

for _ in range(n):
    site, pw = map(str, sys.stdin.readline().split())

    dic[site] = pw

for _ in range(m):
    x = str(sys.stdin.readline().strip())
    print(dic[x])

