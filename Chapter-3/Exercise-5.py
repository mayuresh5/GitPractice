name= input ('enter your name: ')
var_temp=''      #This stops the repetation of letters.
i=0
while i < len(name):
    if name[i] not in var_temp:
        var_temp+=name[i]
        print(f'{name[i]} : {name.count(name[i])}')
    i+=1