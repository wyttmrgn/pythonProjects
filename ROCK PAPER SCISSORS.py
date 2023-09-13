
                                          
from random import *                      
                                          
def getCompThrow():                       
                                          
    # 1 = Rock, 2 = Paper, 3 = Scissors   
    return randint(1, 3)                  
                                          
                                    

# Defining main fuction to run the game
def main():

	# Variables to keep track of winner of games
	compWins = 0
	userWins = 0

	# Function to display header
	displayHeader()
		
        # For loop to run game 4 times
	for num in range(1,5):

                # Display options for user
		displayThrowOptions()

		# Get user choice	
		userChoice = eval(input("  Enter choice (1 - 3): "))

		# Stores random computer choice	
		computerChoice = getCompThrow()

		# Converts user and computer integer values to rock/paper/scissors	
		userThrowWord = getThrowWord(userChoice)
		computerThrowWord = getThrowWord(computerChoice)

		# Determines winner of the round	
		winner = determineRoundOutcome(userThrowWord, computerThrowWord)

		# Updates win count for winning player	
		if winner == "u":
			userWins += 1
		elif winner == "c":
			compWins += 1
			
	# Display final winner	
	displayWinner(userWins, compWins)
		
	
# Function to display game header
def displayHeader():
	
	print("{0:>36s}".format(">" * 17 + "<" * 16))
	print()
	print("{0:^38s}".format("ROCK, PAPER, SCISSORS!"))
	print()
	print("{0:>36s}".format(">" * 17 + "<" * 16))
	
	print()
	
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	
	print()

#  Defining function that displays options for the user
def displayThrowOptions():
    

	print("{0:>15s}".format("=" * 13))
	print("{0:^17s}".format("Options"))
	print("{0:>15s}".format("=" * 13))
	print("{0:>11s} {1:>11s} {2:>13s}".format("1. Rock\n", "2. Paper\n", "3. Scissors"))
	print("{0:>15s}".format("=" * 13))

	print()

# Defining function that converts choice to corresponding type	
def getThrowWord(optionChoice):


	if optionChoice == 1:
		
		optionChoice = "Rock"
		
	elif optionChoice == 2:
		
		optionChoice = "Paper"
		
	elif optionChoice == 3:
		
		optionChoice = "Scissors"
		
	return optionChoice
	

# Defining function that displays winner based on user and computer choice
def determineRoundOutcome(userThrowWord, computerThrowWord):
	
	print()
	print("{0:>16s} {1:>19s}".format("=" * 14, "=" * 14))
	print("{0:>3s} {1:^10s} {2:>0s} {3:>6s} {4:^10s} {5:>0s}".format("|", "USER", "|", "|", "COMPUTER", "|"))
	print("{0:>16s} {1:^4s} {2:>0s}".format("|------------|", "VS", "|------------|"))
	print("{0:>3s} {1:^10s} {2:>0s} {3:>6s} {4:^10s} {5:>0s}".format("|", userThrowWord, "|", "|", computerThrowWord, "|"))
	print("{0:>16s} {1:>19s}".format("=" * 14, "=" * 14))
	print()
	
	winner = ""
	
	
	if userThrowWord == "Rock" and computerThrowWord == "Paper":
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * COMPUTER  WINS! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "c"
		
	elif userThrowWord == "Paper" and computerThrowWord == "Rock":
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * USER  WINS! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "u"
	
	elif userThrowWord == "Rock" and computerThrowWord == "Rock":
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * TIE! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "t"
		
	elif userThrowWord == "Paper" and computerThrowWord == "Scissors":
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * COMPUTER  WINS! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "c"
		
	elif userThrowWord == "Scissors" and computerThrowWord == "Paper":
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * USER  WINS! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "u"
		
	elif userThrowWord == "Paper" and computerThrowWord == "Paper":
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * TIE! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "t"
	
	elif userThrowWord == "Scissors" and computerThrowWord == "Rock":
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * COMPUTER  WINS! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "c"
		
	elif userThrowWord == "Rock" and computerThrowWord == "Scissors":
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * USER  WINS! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "u"
		
	else:
		
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		print("{0:^39s}".format("* * * TIE! * * *"))
		print()
		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print()
		winner = "t"
		
	return winner
	
# Defining function that displays winner based on wins
def displayWinner(userWins, compWins):
	
	if userWins > compWins:
		
		print()
		print("{0:^39s}".format("* * * * * * *"))
		print("{0:>12s} {1:>15s}".format("*", "*"))
		print("{0:>11s} {1:>13s} {2:>3s}".format("*", "USER  WINS!", "*"))
		print("{0:>12s} {1:>15s}".format("*", "*"))
		print("{0:^39s}".format("* * * * * * *"))
	
	elif userWins < compWins:
		
		print()
		print("{0:^39s}".format("* * * * * * * * *"))
		print("{0:>10s} {1:>19s}".format("*", "*"))
		print("{0:>9s} {1:>17s} {2:>3s}".format("*", "COMPUTER  WINS!", "*"))
		print("{0:>10s} {1:>19s}".format("*", "*"))
		print("{0:^39s}".format("* * * * * * * * *"))
		
	elif userWins == compWins:
		
		print()
		print("{0:^39s}".format("* * * * * * *"))
		print("{0:>12s} {1:>15s}".format("*", "*"))
		print("{0:>11s} {1:>9s} {2:>7s}".format("*", "TIE", "*"))
		print("{0:>12s} {1:>15s}".format("*", "*"))
		print("{0:^39s}".format("* * * * * * *"))
		
	

# Calling main function
main()
