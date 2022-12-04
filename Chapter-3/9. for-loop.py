for i in range(1,11):
    print('hello world',i)


num= input('enter the no.: ')
total=0
for i in range(len(num)):
    total+=int(num[i])
    i+=1
print(total)
            
            #OR

num= int(input('enter no.: '))
total=0
for i in range(num+1):
    total+=i
    i+=1
print(total)