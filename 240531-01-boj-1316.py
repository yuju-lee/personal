n = int(input())
cnt = n

for i in range(n):
    s = list(map(str,input()))
    for j in range(len(s)-1):
        if 2 < len(s): #2글자까진 무조건 그룹단어
            if s[j]==s[j+1]:
                continue
            elif s[j] in s[j+1:]:
                cnt = cnt-1
                break
        else:
            pass

print(cnt)
