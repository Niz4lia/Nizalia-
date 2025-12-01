# adventure_retry.py

def crossroad():
    while True:
        choice = input("\nYou're at a crossroad. Go LEFT or RIGHT? ").lower()
        if choice == "left":
            return river()
        elif choice == "right":
            print("😱 You fell into a hole! Try again.")
        else:
            print("Please choose LEFT or RIGHT.")

def river():
    while True:
        choice = input("\nYou find a river. SWIM across or WAIT for a boat? ").lower()
        if choice == "swim":
            print("💀 You were attacked by a crocodile! Try again.")
        elif choice == "wait":
            return doors()
        else:
            print("Please choose SWIM or WAIT.")

def doors():
    while True:
        choice = input("\nYou arrive safely. Choose a door: RED, BLUE, or YELLOW: ").lower()
        if choice == "yellow":
            print("🎉 You found the treasure! YOU WIN!")
            break
        elif choice == "red":
            print("🔥 The room is full of fire! Try again.")
        elif choice == "blue":
            print("🐉 A dragon eats you alive! Try again.")
        else:
            print("That door doesn't exist. Choose RED, BLUE, or YELLOW.")

def start_game():
    print("🏰 Welcome to the Adventure Quest!")
    print("Your goal: find the hidden treasure in the forest.\n")
    crossroad()

while True:
    start_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break
