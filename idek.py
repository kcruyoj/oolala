secret = "YES"
guess_count = 1
print("You only get three chances to guess the word.")
trial = 3

while guess_count <= 3:
    guess = input("Enter the word: ")
    guess = guess.upper()
    if guess == secret:
        print("You guessed the secret word right.") 
breakpoint
    else:
        trial = trial - 1
        if trial == 2:
            print(f"The guess is wrong. You still have {trial} more tries.")
        else:
            print(f"The guess is wrong. You still have {trial} more try.")
    guess_count += 1
