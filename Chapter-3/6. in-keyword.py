statement= input('enter statement: ')
keyword= input('enter keyword: ')
if keyword in statement:
    print('total no.:',statement.count(keyword))