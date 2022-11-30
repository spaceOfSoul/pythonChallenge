# f = open("asd.txt", 'r')
count = {}

with open("asd.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        for i in line:
            if count.get(i) is not None:
                count[i] +=1
            else:
                count[i] = 1

result = 999999999
resultStr = ''
for i in count:
    if count[i] < result:
        result = count[i]
        resultStr = i
    elif count[i]==result:
        resultStr+=i
    

print(resultStr, result)