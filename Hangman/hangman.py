import random

easy_words = ["cat", "dog", "apple", "money", "monkey","book","pen","quiz"]
medium_words = ["banana", "chair", "chest", "chess", "dragon", "elephant", "lucky", "funny", "wave"]
hard_words = ["uptown", "vortex", "wavy", "hurry", "rhythm", "strength", "strengths", "subway", "jazz",
"injury", "jumbo", "luxury", "matrix", "oxygen", "pixel", "gossip", "duplex", "galaxy", "sphinx", "razzmatazz"]

def hang(mistake):
    if mistake == 0:
        print("   ______")
        print("  |      ")
        print("  |      ")
        print("  |     ")
        print("  |     ")
        print("__|__")
    elif mistake == 1:
        print("   ______")
        print("  |      |")
        print("  |      ")
        print("  |     ")
        print("  |     ")
        print("__|__")
    elif mistake == 2:
        print("   ______")
        print("  |      |")
        print("  |      o")
        print("  |     ")
        print("  |     ")
        print("__|__")
    elif mistake == 3:
        print("   ______")
        print("  |      |")
        print("  |      o")
        print("  |     /")
        print("  |     ")
        print("__|__")
    elif mistake == 4:
        print("   ______")
        print("  |      |")
        print("  |      o")
        print("  |     / \\")
        print("  |     ")
        print("__|__")
    elif mistake == 5:
        print("   ______")
        print("  |      |")
        print("  |      o")
        print("  |     /|\\")
        print("  |     ")
        print("__|__")

    elif mistake == 6:
        print("   ______")
        print("  |      |")
        print("  |      o")
        print("  |     /|\\")
        print("  |     /")
        print("__|__")
    elif mistake == 7:
        print("   ______")
        print("  |      |")
        print("  |      o")
        print("  |     /|\\")
        print("  |     / \\")
        print("__|__")


print("**********          THE HANGMAN          **********")
print("___________________________________________________")
print("""
Game Rules:
- each rund you can guess a letter
- guess all the letters to win
- if you guess wrong for 7 times you'll be handged and the game is over
""")
print("___________________________________________________")

game_words_set = []
difficulty_level = input("""Please select the game difficulty level(e/m/h)
- Enter e for easy
- Enter m for medium
- Enter h for hard \n""")
while True:
    if difficulty_level.lower() == "e":
        game_words_set = easy_words
        break
    elif  difficulty_level == "m":
        game_words_set == medium_words
        break
    elif  difficulty_level == "h":
        game_words_set == hard_words
        break
    else:
        difficulty_level = input("Please select one of these levels(e/m/h) \n")
        

min_index = 0
max_index = len(game_words_set) - 1
mistakes = 0

random_index = random.randint(min_index, max_index)

random_word = game_words_set[random_index]

random_word_letters = list(random_word)

number_of_letters = len(random_word)

lines = list("_" * number_of_letters)

print("  ".join(lines))
while "_" in lines:
    guess = input("guess a letter: ")
    if guess in random_word_letters:
        # print(random_word_letters.index(guess))
        if guess in lines:
            print("you have guessed this letter before, please guess a new letter.")
        else:
            for i in range(len(random_word_letters)):
                if random_word_letters[i] == guess:
                    
                    lines[i] = guess 
                
            print("  ".join(lines))
            hang(mistakes)
    else:
        mistakes += 1
        print("{} is not in the word, please guess again!".format(guess))
        hang(mistakes)
    if mistakes == 7 :
        print("I'm sorry, you are out of guesses :(")
        
        break
if mistakes < 7:
    print("You Win!")
else:
    print("Gameover!")