import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        print("Congratulations, you guessed the number!")
        break

for i in range(10):

    print(i+2)

    print(i+3,"hello")
