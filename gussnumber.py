import random


number = random.randint(1,10)
print(f'''
-----------------------------
Correct answer: {number}
-----------------------------
    ''')
attempt = 3
msg = ''

while attempt > 0:
    user=  int(input('Enter Number: '))
    if number == user:
        #print('Wooooooooooooola')
        msg = 'You Won!'
        break
    elif user > number:
        print(f"{user} is greater.\n Remaning attempts: {attempt}.")
        attempt -= 1
    elif user < number:
        print(f"{user} is smaller.\n Remaning attempts: {attempt}.")
        attempt -= 1

    else:
        print('Something went Wrong')
        break

print(msg)







