n, b = list(map(int,input().split()))

dic = dict()

cnt = 10
for i in range(65, 91):
    dic.setdefault(cnt,chr(i))
    cnt = cnt+1

ans = ''
while n:
    if 10 <= n%b:
        ans = ans+str(dic[n%b])
    else:
        ans = ans+str(n%b)
    n //= b

print(ans[::-1])