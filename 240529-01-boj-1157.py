s = str(input()).upper()
ls = list(s)
dic = {}

for i in range(65,91): 
    dic.setdefault(i, 0)

for i in range(len(ls)):
    a = ord(ls[i])
    value = dic[a]
    dic[a] = value + 1

dicvalues = list(dic.values())
maxdata = max(dicvalues)

maxindex = list(filter(lambda x: dicvalues[x] == maxdata, range(len(dicvalues))))

if len(maxindex) > 1:
    print("?")
else:
    print(chr(maxindex[0]+65))