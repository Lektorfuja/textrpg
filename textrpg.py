import random

def print_header():
    print("==========================")
    print(" Welcome to the Text RPG")
    print("==========================")

def choose_character():
    print("Choose your character:")
    print("1. Warrior - High health, medium damage")
    print("2. Mage - Low health, high damage")
    print("3. Rogue - Medium health, high critical chance")

    choice = input("Enter the number of your choice: ")
    if choice == "1":
        return {"class": "Warrior", "health": 120, "damage": 10, "crit": 5}
    elif choice == "2":
        return {"class": "Mage", "health": 80, "damage": 15, "crit": 10}
    elif choice == "3":
        return {"class": "Rogue", "health": 100, "damage": 12, "crit": 20}
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return {"class": "Warrior", "health": 120, "damage": 10, "crit": 5}

def encounter_enemy():
    enemies = [
        {"name": "Goblin", "health": 50, "damage": 5},
        {"name": "Orc", "health": 80, "damage": 8},
        {"name": "Dark Wizard", "health": 60, "damage": 12},
    ]
    return random.choice(enemies)

def battle(player, enemy):
    print(f"\nYou encounter a {enemy['name']}!")
    print(f"{enemy['name']} has {enemy['health']} health.")

    while player["health"] > 0 and enemy["health"] > 0:
        print("\nYour turn:")
        action = input("Choose an action: [A]ttack or [H]eal: ").lower()

        if action == "a":
            if random.randint(1, 100) <= player["crit"]:
                damage = player["damage"] * 2
                print("Critical hit!")
            else:
                damage = player["damage"]

            enemy["health"] -= damage
            print(f"You deal {damage} damage to the {enemy['name']}.")
        elif action == "h":
            heal = random.randint(8, 15)
            player["health"] += heal
            print(f"You heal for {heal} health.")
        else:
            print("Invalid action. You lose your turn.")

        if enemy["health"] > 0:
            print(f"\n{enemy['name']}'s turn:")
            player["health"] -= enemy["damage"]
            print(f"The {enemy['name']} deals {enemy['damage']} damage to you.")

        print(f"\nYour health: {player['health']}")
        print(f"{enemy['name']}'s health: {enemy['health']}")

    if player["health"] > 0:
        print(f"\nYou defeated the {enemy['name']}!")
        return True
    else:
        print("\nYou have been defeated. Game over.")
        return False

def main():
    print_header()
    player = choose_character()
    print(f"You have chosen the {player['class']} class. Good luck, hero!\n")

    while True:
        enemy = encounter_enemy()
        if not battle(player, enemy):
            break

        print("\nYou take a moment to rest and recover.")
        rest = random.randint(10, 20)
        player["health"] += rest
        print(f"You regain {rest} health. Your current health is {player['health']}.\n")

        continue_game = input("Do you want to continue your adventure? (yes/no): ").lower()
        if continue_game != "yes":
            print("\nYou retire as a hero. Thanks for playing!")
            break

if __name__ == "__main__":
    main()
