name= input ('enter your name: ')
age= input ('Enter your age: ')
age=int(age)
if (name[0] == 'A' or name[0] == 'a') and age>=10:
    print('you can watch TV')
else:
    print('Permission denied!')