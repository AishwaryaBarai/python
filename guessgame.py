secret_num = 9
count = 0
while count < 3:
    guess = int(input('enter your guess: '))
    count = count + 1
    if guess == secret_num:
        print('you win !')
        break
    else:
        print('you lost')

