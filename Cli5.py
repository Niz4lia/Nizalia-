# detective_game.py

print("🕵️ DETECTIVE MYSTERY GAME 🩸")
print("A rich man was found dead in his mansion last night.")
print("You, the detective, must find out who did it!\n")

suspects = ["Chef", "Butler", "Maid"]
clues_found = []
murderer = "Butler"  # The real culprit

while True:
    print("What would you like to do?")
    print("1. Question a suspect")
    print("2. Check clues")
    print("3. Make final accusation")
    print("4. Quit")
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        print("\nWho do you want to question?")
        for s in suspects:
            print("-", s)
        name = input("Enter suspect name: ").title().strip()

        if name == "Chef":
            print("\n👨‍🍳 Chef: 'I was cooking dinner all night! I heard a loud thud around 9 PM.'\n")
            clues_found.append("Chef heard a noise at 9 PM")
        elif name == "Butler":
            print("\n🤵 Butler: 'I was cleaning the study. The knife from the kitchen was missing... strange.'\n")
            clues_found.append("Butler mentioned missing knife")
        elif name == "Maid":
            print("\n👩 Maid: 'I saw the Butler sneaking toward the kitchen before dinner!'\n")
            clues_found.append("Maid saw Butler sneaking")
        else:
            print("\n❌ That person isn’t a suspect!\n")

    elif choice == "2":
        if clues_found:
            print("\n🧾 Clues you’ve found so far:")
            for c in clues_found:
                print("-", c)
            print()
        else:
            print("\nYou haven’t found any clues yet.\n")

    elif choice == "3":
        guess = input("Who do you think is the murderer? ").title().strip()
        if guess == murderer:
            print("\n🎉 Correct! The Butler was guilty — he tried to cover it up!")
            print("You solved the case, Detective! 🏆")
            break
        else:
            print("\n❌ That’s not correct, Detective. Keep investigating!\n")

    elif choice == "4":
        print("\n🚪 You left the case unsolved. Goodbye, Detective.")
        break

    else:
        print("\nInvalid choice. Try again.\n")
