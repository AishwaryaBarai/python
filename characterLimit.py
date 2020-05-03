name = input('enter your name: ')
length = len(name)
if length >3 and length <50:
    print('we are good to go :)')
if length< 3:
    print('name must be atleast 3 characters !')
elif length > 50:
    print('name must be less than 50 characters !')
