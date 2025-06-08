import random  # type: ignore
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    name = input("What is your name? ").strip()
    while not name:
        name = input("Please enter a valid name: ").strip()
    
    choice = input(f"Are you sure your name is {name}? (Yes/No) ").lower()
    if choice == "yes":
        intro(name)
    elif choice == "no":
        start_game()

def intro(name):
    clear()
    
    slow_print(f"Wake up, {name}! Wake up!")
    slow_print("A small body crashes onto your bed, jolting you awake. It's your little brother, Eli, bouncing on top of you.")
    slow_print("'Get OFF, you little goblin!' you groan, pushing him away. 'Don’t you have Mom to annoy?'")
    
    slow_print("Eli giggles, unfazed. 'Oh yeah!' he shouts before sprinting off, leaving you in peace.")

    slow_print("With a sigh, you sit up, rubbing the sleep from your eyes. The scent of pancakes fills the air, pulling you toward the kitchen.")

    clear()
    slow_print("You drag yourself into the kitchen, where Mom is humming softly, flipping golden pancakes.")
    slow_print(f"She turns, holding an envelope sealed with shimmering gold wax. 'This came for you, {name}. It’s from the Academy.'")

    slow_print("Your heart skips a beat. The Academy? You snatch the envelope, breaking the seal with trembling fingers.")

    slow_print("As you unfold the parchment, elegant, swirling text reveals itself:")

    slow_print(f"Dear {name},")
    slow_print("You have been selected to participate in the prestigious Tournament of Elders—a competition that brings forth the greatest magical talents of our time.")
    slow_print("Your presence is requested at the Celestial Arena within three days.")
    slow_print("The fate of magic itself may rest in your hands.")
    slow_print("Prepare yourself. Destiny awaits.")

    slow_print("Your breath catches. The Tournament of Elders—only the strongest mages receive an invitation.")

    slow_print("Without another thought, you bolt toward the door, adrenaline surging.")

    slow_print("'Hold on!' Mom calls out. 'At least put some clothes on before you run to the arena!'")

    slow_print("Realizing your mistake, you hurry back inside, throwing on the first outfit you can find. Once dressed, you sprint toward Kyle’s house.")

    clear()
    slow_print("As you round the corner, you spot Kyle—your best friend—already running outside, a similar letter clutched in his hand.")
    slow_print("Neither of you are paying attention, and—WHAM!—you slam into each other.")

    slow_print("'Oof!' Kyle stumbles back, shaking his head. 'Did you get the invitation?!'")
    slow_print("'Heck yeah!' you exclaim, holding yours up.")

    slow_print("A grin spreads across Kyle’s face. 'Then what are we waiting for?'")
    slow_print("Without another word, the two of you take off toward the Celestial Arena, racing to see who can get there first.")

    arena_arrival(name)

def arena_arrival(name):
    clear()
    slow_print("As you approach the towering gates of the Celestial Arena, the air hums with magic.")
    slow_print("The grand golden spires reach into the heavens, glowing with ancient energy.")
    
    slow_print(f"'This is insane,' Kyle whispers, his voice filled with awe.")
    
    slow_print("The massive entrance doors creak open, revealing a vast hall lined with banners of different magical schools.")
    slow_print("Competitors stand in clusters, exchanging introductions or eyeing each other warily.")
    
    meet_competitors(name)

def meet_competitors(name):
    clear()
    slow_print("You scan the room, recognizing a few famous faces from stories and legends.")
    
    competitors = [
        {"name": "Lady Veyna", "description": "A regal sorceress draped in flowing robes. Her piercing gaze seems to read minds."},
        {"name": "Drakar the Warlord", "description": "A battle mage with scars marking every fight he’s survived. His presence demands respect."},
        {"name": "Zyra Moonshadow", "description": "A rogue spellcaster who thrives on deception and illusion."},
        {"name": "The Shadowed One", "description": "A masked figure standing alone. No one knows their origins, only their terrifying power."}
    ]
    
    for competitor in competitors:
        slow_print(f"You spot {competitor['name']}. {competitor['description']}")
    
    slow_print(f"Kyle nudges you. 'Man, this is wild. Do you think we even stand a chance, {name}?'")
    
    slow_print("Before you can respond, a deep, commanding voice silences the room.")

    tournament_announcement(name)

def tournament_announcement(name):
    clear()
    slow_print("A figure steps forward—a towering overseer dressed in ceremonial armor, his staff crackling with ancient magic.")
    slow_print("'WELCOME, CHAMPIONS!' his voice booms through the hall.")
    
    slow_print("'You have been chosen to compete in the Tournament of Elders—a battle of skill, intellect, and destiny!'")
    slow_print("'Only one among you will emerge victorious and claim the title of Grand Magus!'")
    
    slow_print("The room is still, the weight of his words settling on every participant.")

    slow_print("'Prepare yourselves. Your first challenge begins at sunrise.'")
    
    slow_print("Kyle grips his letter tightly, determination flashing in his eyes. 'This is it, {name}… Tomorrow, it all begins.'")
    
    first_challenge(name)

def first_challenge(name):
    clear()
    slow_print("The next morning, the sun rises over the Celestial Arena, bathing the hall in golden light.")
    
    slow_print("You and Kyle stand among the competitors, waiting for the first challenge to be announced.")
    
    slow_print("The overseer returns, his presence commanding all attention.")
    
    slow_print("'The first challenge will test your ability to wield magic under pressure.'")
    slow_print("'You will navigate the **Labyrinth of Trials**—a shifting maze filled with illusions, traps, and arcane puzzles.'")
    
    slow_print("'Make it to the center before sunrise… or be eliminated.'")
    
    slow_print(f"Kyle glances at you. 'Ready for this, {name}?'")
    
    slow_print("The doors to the labyrinth slowly begin to open...")

start_game()