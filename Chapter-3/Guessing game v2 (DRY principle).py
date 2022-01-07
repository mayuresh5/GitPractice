import random
winning_number= random.randint(1,100)
num= int(input('enter the no. from 1 to 100: '))
guess=1
while True:
    if num==winning_number:
        print(f'you win!! And you win in {guess} times.')
        break
    else:
        if num < winning_number:
            print('too low')
        else:
            print('too high')
        num= int(input('enter again: '))
        guess+= 1