import os
import time
import random  # type: ignore

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    name = input("What is thy name, peasant? ").strip()
    slow_print(f"Welcome, {name}! Prepare thyself for an adventure...")
    intro()

def intro():
    slow_print(f"")