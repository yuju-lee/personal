from collections import Counter

cnt = int(input())
area = 100*100

barea = cnt*100

def setMatrix (n):
    ls = []
    for i in range(11):
        ls.append(n+i)
    return ls

sumw = []
sumh = []
for i in range(cnt):
    w, h = map(int, input().split())
    lsw = setMatrix(w)
    sumw.append(lsw)
    lsh = setMatrix(h)
    sumh.append(lsh)


print(sumw)
print(sumh)


# 모든 값을 하나의 리스트에 모으기
all_values = [value for sublist in sumw for value in sublist]

# 중복된 값을 찾아내기
count = Counter(all_values)
duplicates = [item for item, freq in count.items() if freq > 1]

print(duplicates)