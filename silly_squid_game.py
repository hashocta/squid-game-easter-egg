import random
import time

# Fun character choices
characters = ['Player 456', 'The Front Man', 'Player 101', 'The Doll', 'The Guard']

def intro():
    print("\nWelcome to the Silly Squid Game!")
    print("You’re stuck in a game where you have to make some funny choices to survive!")
    time.sleep(2)
    print("Can you make it through all the rounds without getting eliminated? Let's find out!")

def choose_character():
    print("\nChoose your character (type the number of your choice):")
    for i, char in enumerate(characters):
        print(f"{i + 1}. {char}")
    choice = int(input("Enter your choice: ")) - 1
    if choice not in range(len(characters)):
        print("Invalid choice! Defaulting to Player 456.")
        return 'Player 456'
    else:
        return characters[choice]

def funny_outcome(character):
    print(f"\nYou chose {character}!")
    time.sleep(1)
    print(f"\n{character} gives you a silly challenge!")
    
    # Random funny outcomes
    outcomes = [
        f"{character} offers you a glass of water, but it's actually a cup of jelly!",
        f"{character} challenges you to a game of rock-paper-scissors... but they only know rock!",
        f"{character} asks you to solve a riddle, but the answer is always 'banana.'",
        f"{character} hands you a toy squid and tells you to 'make it dance.'",
        f"{character} asks you to run 100 meters... in a straight line... backwards!"
    ]
    
    print(random.choice(outcomes))
    time.sleep(2)

def main_game():
    intro()
    character = choose_character()
    funny_outcome(character)
    
    print("\nThe game continues with more ridiculous choices!")
    time.sleep(2)
    
    # Randomly determine whether the player survives or gets eliminated (based on humor, of course)
    survival = random.choice([True, False])
    if survival:
        print("\nCongratulations! You survived the Squid Game... for now.")
    else:
        print("\nOops! You were eliminated... but it was a very funny way to go out!")
    
    print("\nGame over! Thanks for playing!")
    time.sleep(2)

if __name__ == "__main__":
    main_game()
