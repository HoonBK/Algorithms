t = int(input())

fb = [(1,0), (0,1)]

for x in range(2,42):
    fb.append((fb[x-1][0] + fb[x-2][0] , fb[x-1][1] + fb[x-2][1] ))

for _ in range(t):
    a = int(input())
    print (fb[a][0], fb[a][1])