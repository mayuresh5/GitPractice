userid= input ('enter your user id.:  ')
password = input ('enter your password:  ')
if userid== 'mayureshg08' and password== '08091995.':
    print('Access granted!')
else:
    if userid== 'mayureshg08' or password== '':
        print('You need to reset your password')
    elif userid== '' or password== '08091995.':
        print('Check your mail id!')
    else:
        print('Access denied!')
    