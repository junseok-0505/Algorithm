# 이코테 Part3 1-3

s = input()
count0 = 0
count1 = 0
data = [int(i) for i in s]

if data[0] == 1:
    count0 += 1
else:
    count1 += 1
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == 1: 
            count0+=1
        else:
            count1+=1
            
print(min(count0, count1))
