# Rock Paper Scissors
import random

userWins = 0
computerWins = 0

options = ['rock', 'paper', 'scissors']

while True:
	userInput = input("Type 'Rock/Paper/Scissors' or 'q' to quit: ").lower()
	if userInput == 'q':
		break

	if userInput not in options:
		print("Error, please try again.")
		continue
	randNum = random.randint(0,2)
	# rock: 0, paper: 1. scissors: 2
	computerPick = options[randNum]
	print('Computer picked', computerPick+'.')
	if userInput == 'rock' and computerPick == 'scissors':
		print('You won!')
		userWins += 1
		continue
	elif userInput == 'paper' and computerPick == 'rock':
		print('You won!')
		userWins += 1
		continue
	elif userInput == 'scissors' and computerPick == 'paper':
		print('You won!')
		userWins += 1
		continue
	elif userInput == computerPick:
		print("It's a tie!")
		continue
	else:
		print('You lost!')
		computerWins += 1

print('You won', userWins, 'times.', '\nThe computer won', computerWins, 'times.')
print('Goodbye!')



























