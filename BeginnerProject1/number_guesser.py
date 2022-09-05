import random

print("""\nWelcome to the guessing game!\n""")

rangeMax = input("""Please type a max number: """)
if rangeMax.isdigit():
    rangeMax = int(rangeMax)

    if rangeMax <= 0:
        print("Please typer a positive numnber.")    
        quit()
 #   elif
else: 
    print("Please type a number.")
    quit()

random_number = (random.randint(0, rangeMax))
#print(random_number)
print("""\n---------------------------\nNow guess what the random number is. It will be between 0 and your number!
Have fun!""")
guesses = 0
while True:
    guesses += 1
    userGuess = input("Make a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else: 
        print("Please type a number.")
        continue
    
    if userGuess == random_number:
        print("You got it!")
        break    
    elif userGuess > random_number:
        print("You guessed greater than the number.")
    else:
        print("You guessed less than the number.")
    continue

if guesses == 1:
    print("you got the answer in", guesses, "guess.\n")
else:
    print("you got the answer in", guesses, "guesses.\n")





























