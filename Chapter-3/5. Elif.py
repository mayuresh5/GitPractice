age= input('enter your age: ')
age = int(age)
if 0<age<= 3:
    print("Entry is free!")
elif 4<age<=10:
    print("Entry fee: Rs.100")
elif 11<age<=60:
    print("Entry fee: Rs.250")
elif age >=60:
    print("Entry fee: Rs.200")
elif age==0:
    print('You cant watch!')