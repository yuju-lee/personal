cnt = int(input())

# 100*100 배열 만들기
white = [[0 for x in range(101)]for y in range(101)]
blackcount = 0

#가로 세로 10칸씩 숫자 올리기
#중복 생각하지 않고 그냥 무조건 칠한 곳은 1로 생각하면 되는거엿음... 하...
for i in range(cnt):
    w, h = map(int, input().split())
    for j in range(0, 10):
        for k in range(0, 10):
            white[j+w][k+h] = 1

for i in range(0,101):
    blackcount += white[i].count(1)

print(blackcount)