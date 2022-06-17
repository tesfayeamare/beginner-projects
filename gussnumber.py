import random
number = random.randint(1,10)
print('welcome to Guess the Numbert Game')

for i in range(0,3):
    user=  int(input('Guess a number '))
    if number == user:
        print('Wooooooooooooola')
        print(f'You gussed the number right it is {number}')
        break
if number != user:
    print(" You guessd wrong number sorry ")
    print(" Try Againnnnnnnnnn")
    