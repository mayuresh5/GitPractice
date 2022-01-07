guess = input('enter any no. from 1 to 10:  ')
guess = int(guess)
if guess == 7:
    print('You rock!')
else:
    if guess< 7:
        print('low')
    else:
        print('high')