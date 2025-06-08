import random # type: ignore
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.05):
	for char in text:
		print(char, end='', flush=True)
		time.sleep(delay)
	print()

def start_game():
	clear()
	slow_print("A man in striped clothes walks up to you and says: 'Hello and welcome to Argders land of cool sigma stuff!'")
	slow_print("Please enter and wait to be sigmaified.")
	choice = input("Do you 1, enter, or 2, punch the man in the face and run away whilst screaming bloody murder? ")
	if choice == "1":
		enter()
	elif choice == "2":
		slow_print("You put up your dukes and throw a big one, but he dodges and molly-whops your booty. game over duderino.")
		start_game()
	else:
		print("no")
		start_game()	

def enter():
	clear()
	slow_print("You follow the man and wait patiently.")
	slow_print("After a few minutes of waiting, the man comes back and says 'Thank you for your patience, please come with me!'")
	choice = input("Do you 1, come with him and say nothing, or 2, say 'Nah man I dont even know you.' and get the flip out of there? ")
	if choice == "1":
		follow()
	elif choice == "2":
		slow_print("He says too bad and lifts up his shirt to reveal a glock 17. You say 'My bad I meant: 'Sure I'll go with you!''")
		follow()
	else:
		print("no")
		enter()

def follow():
	clear()
	slow_print("You follow the man into a extremely long hall way.")
	slow_print("The man introduces himself as Frank, Frank talks about how excited he his for you to be sigmafied by Argder.")			
	slow_print("At the end of the hallway, Frank stops you and tells you to look sharp and mind your manners.")
	choice = input("Do you 1, look sharp and mind your manners, or 2, roll up your sleeves and say 'No I'm good' ")
	if choice == "1":
		argder()
	elif choice == "2":
		slow_print("'Your funeral.'")
		argder()
	else:
		slow_print("no")
		follow()	

def argder():
	clear()
	slow_print("You walk into a large room with a domed roof, you didnt see this on the outside. There is a large chair in the middle of the room, there is a friendly looking man sitting in it")
	slow_print("You look around for Frank for guidance, but he is gone")
	slow_print("The man in the chair says 'Well, hello there! How may Argder help you today?'")
	choice = input("Do you 1, yell and run down the hallway from whence you came, or 2, say 'I came for help on controlling my anger.'? ")
	if choice == "1":
		slow_print("Frank is waiting at the end of the hall and demands you get back in there.")
		argder()
	elif choice == "2":
		slow_print("Argder says 'Well, Argder can help with that!'")
		slow_print("You begin to fly in the air, when your head almost reaches the roof, a bright light emits from Argder and soon you can no longer see.")
		slow_print("After the light has faded and you can see once more, you begin to feel more relaxed...")
		slow_print("Maybe Argder was as powerful as the rumors said...")
		ending()

def ending():
	clear()
	slow_print("You walk back out the hallway and Frank is waiting for you at the end.")
	slow_print("'How'd it go?'")
	slow_print("You say 'Remarkable!'")
	slow_print("Frank says 'Tell your friends, the great Argder is open to all!'")    	
	
start_game()


