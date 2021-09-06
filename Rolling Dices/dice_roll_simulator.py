import random

min_val = 1
max_val = 6


# validate the input
def input_validation(answer):
    while True:
        if answer.lower() == "no" or answer.lower() == "n":
            print("GoodBye")
            break
        elif answer.lower() == "yes" or answer.lower() == "y":
            answer = "yes"
            break
        else:
            answer = input("Try Again the Answer Must be yes or no: ")
    return answer
    # return roll_again


roll_again = input("Ready for Rolling the Dices? (yes/no) \n")

# validate the input
roll_again = input_validation(roll_again)

while roll_again == "yes" or roll_again.lower() == "y":
    print("Rolling Dices...")
    print("The Values Are: ")

    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    roll_again = input("Roll the Dices Again? (yes/no)")
    
    # validate the input
    roll_again = input_validation(roll_again)
