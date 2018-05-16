#Laura Davis
#This is a practice program that asks a variety of questions and reads back answers. 
#Includes a guessing game.
#this program is separated into several functions.
#input is for numbers and raw_input is for strings in this version of python.
#float() is used to always display Reals. 

def main(): 

#this section introduces the program and asks user for name input.
	print "Hello. My name's Patience."
	myName = raw_input("What is your name? ")
	print "Hello,",myName,"! "
#declared variables
	myAge = run_age()
	food = fav_food()
	IAm = how_ru()
	gameYn = play_game()
	
#this section asks for an age and rejects it if it's out of range.
#if/then loops require while True and try, followed by except and break.
#For this to loop back, else condition must be met and properly indented. 
#Breaks must be included or first statement is found True and it results in an infinite loop. 
#ints and strings must be declared in this type of mixed statement. 
def run_age():
	while True:
		try: 
			myAge = int(input("How old are you? "))
			print ("You are"), str(myAge) +(" years old. ")
		except NameError:
			print "That can't be right. "
		else:
			if 1 <= myAge <= 125:
				break
			else:
				print "That can't be right. "
				print "Please re-enter your age. "
			
#this section asks for and prints your favorite food. Naturally, your new BFF agrees with you.
def fav_food():
	food = raw_input("What is your favorite food? ")
	print "I like", food, "too! "
	
#This section asks how you are doing today and simulates concern upon user response. 
#See? If you don't have friends, you can always program them. 
#elif can only be related to if, and else can only be related to if. 
#might be able to improve this later on.
def how_ru():
	IAm = raw_input("How are you doing today? ") 
	if (IAm == "good") or (IAm == "Good") or (IAm == "fine") or (IAm == "Fine"):
		print "Great! "
	elif (IAm == "bad") or (IAm == "Bad"):
		print "It will get better! "
	elif (IAm != "good") or (IAm != "Good") or (IAm != "fine") or (IAm != "Fine") or (IAm != "bad") or (IAm != "Bad"):
		print "Huh? " 
	print #blank line
		
#this section invites you to play a simple guessing game. 
#If user answers yes, the game initializes. If user answers no, the program exits.
#multiple conditions in if/then statements require each variable equal or not to each condition
#in parentheses. Parens must be separated by "or" or "and".
#return exits the program cleanly and returns to command line. 
def play_game():
	gameYn = raw_input("Do you want to play a guessing game? ")
	if (gameYn == "no") or (gameYn == "No"):
			print "Okay. Bye! "
			print #blank line
			return
	elif (gameYn == "yes") or (gameYn == "Yes"):
		print ("Yay! ")
		print #blank line
	guessingGame = raw_input ("Guess a number between 1 and 10. ")
	
#typing main() in the command line re-runs the program. 
main ()	
