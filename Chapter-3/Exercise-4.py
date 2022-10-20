num= input('Enter the no.: ')
total=0
i=0
while i<len(num):         # for i in range(len(num)):
    total+= int(num[i])
    i+=1
print(total)