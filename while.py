secret_number = 5
guess_count = 0
while guess_count < 3:
    guess = int(input('Guess a number: '))
    guess_count +=1
    if guess == secret_number:
        print('Congratulations! You Won')
        break
    elif guess != secret_number:
        print('Sorry, you can try again')
else:
    print('Sorry, You Failed')