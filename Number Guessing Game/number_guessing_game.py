import  random

print("**********          Number Guessing Game          **********")
print("____________________________________________________________")
print("""The cumputer will choose a number between 1 and 200 and you
have 7 chanse to guess the correct number.
Good Luck """)
print("____________________________________________________________")

min_number = 1
max_number = 200

random_number = random.randint(min_number, max_number)

rounds = 0


while rounds < 7:
    print("Round {}".format(rounds+1))

    guess = int(input("guess a number: "))
    if guess == random_number:
        print("You Win!")
        break
    elif guess < random_number:
        if(random_number - guess) < 10:
            print("You are close, you should guess a bigger number!")
        else:
            print("Too low!!!")
    elif guess > random_number:
        if(guess - random_number) < 10:
            print("You are close, you should guess a smaller number!")
        else:
            print("Too high!!!")
    
    rounds += 1

if rounds == 7:

    print("Game over :(")

