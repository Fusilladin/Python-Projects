# Choose your own adventure game

name = input("Type your name: ")
print("Welcome", name, "to this adventure!\n")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. \nWhich way would you like to go? Left/Right: ").lower()

while True:
	if answer == "left":
		answer = input("You come to a river, you can walk around it or swim accross. Walk/Swim: ")
		if answer == 'swim':
			print("You swam across the river and were eaten by an alligator.")
			quit()
		elif answer == 'walk':
			print("You walked for many miles, ran out of water, and died of6 dehydration.")
			quit()
		else:
			print("Not a valid option. You lose.")
			quit()
	elif answer == "right":
		answer = input("You come up to a wobbly wooden bridge. Do you want to cross it? Yes/No: ")
		if answer == 'yes':
			answer = input("You begin crossing the bridge and along the way there is a gap on the wooden planks. \nDo you go back or continue on? Back/Continue: ")
			if answer == 'continue':
				print("You successfully cross the bridge and a villager greets you with food! \nCongrats you found home and won the game!")
				quit()
			elif answer == 'back':
				print("You trip walking backwards on the bridge and fall to your death.")
				quit()
			else:
				print("Not a valid option. You lose.")
				quit()

		elif answer == 'no':
			print("You go back and lose the game.")
			quit()
		else:
			print("Not a valid option. You lose.")
			quit()
	else:
		print("Not a valid option. You lose.")
		quit()

# print("Thank you for playing!")






















