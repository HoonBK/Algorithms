n = int(input())

stair = list()
score = list()

for i in range(n):
    num = int(input())
    stair.append(num)


score.append(stair[0])

if n>1:
    score.append(stair[0]+stair[1])

if n>2:

    if stair[0]>stair[1]:
        score.append(stair[0]+stair[2])
    else:
        score.append(stair[1]+stair[2])

if n>3:

    for i in range(3,n):
        if stair[i-1]+score[i-3] > score[i-2]:
            score.append(stair[i-1]+score[i-3]+stair[i])
        else:
            score.append(score[i-2]+stair[i])

print(score[n-1])