# coding=UTF-8
"""while 语句
以条件为真为前提重复执行某块语句
"""
number = 23
running = True

while running:
    guess = int(input("enter an integer:"))

    if guess == number:
        print("congratulations , you guessed it ")
        running = False
    elif guess < number:
        print(' no , it is a little higher than that')
    else:
        print("mo ,it is a little lower than that")

else:
    print('the while loop is over')