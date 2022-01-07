name,letter= input('enter your name & alphabet you want to search: ').split(',')
print('No. of letters in your name: ',len(name))
# name1=name.lower()
# letter1=letter.lower()
print('No. of choosed letter in your name: ',name.strip().lower().count(letter.strip().lower()))    #STRIP METHOD TO SOLVE SPACE RELATED PROBLEM