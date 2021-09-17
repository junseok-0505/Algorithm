s = input()
text = []
num = []
for i in s:
    try:
        a = int(i)
        num.append(a)
    except:
        text.append(i)
        
result = sorted(text)+sorted(num)
for j in result:
    print(j,end='')