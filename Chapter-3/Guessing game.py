winning_number=43
num= int(input('enter the no. from 1 to 100: '))
guess=1
game_over= False
while not game_over:
    if num==winning_number:
        print(f'you win!! And you win in {guess} times.')
        game_over= True
    else:
        if num < winning_number:
            print('too low')
            num= int(input('enter again: '))
            guess+= 1
        else:
            print('too high')
            num= int(input('enter again: '))
            guess+= 1