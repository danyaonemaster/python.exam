import random

player_hp = 0
player_mana = 0
enemy_hp = 0


def movement():
    global player_hp, player_mana, enemy_hp

    def characteristics(class_character):
        match class_character:
            case "magician":
                return [1200, 380, 450, 1200]
            case "warrior":
                return [1800, 450, 700, 500]
            case "robber":
                return [900, 500, 300, 700]
            case _:
                print("Invalid class")
                return None

    def character():
        name = input("Enter your name: ")
        class_character = input("""Enter your class:
        magician: hp:1200 atk:380 def:450 mana; 1200
        warrior: hp:1800 atk:450 def: 700 mana: 500
        robber: hp:900 atk: 500 def: 300 mana: 700
        """)
        return name, class_character

    def enemy():
        enemies = {
            "slime": [500, 150, 200],
            "skeleton": [800, 300, 300],
            "goblin": [700, 200, 250],
        }
        enemy_type = random.choice(list(enemies.keys()))
        return enemy_type, enemies[enemy_type]

    def character_atk(character_class, character_atk, character_mana, character_hp, enemy_hp):
        if character_class == "warrior":
            print("Warriors cannot attack!")
            return "invalid", character_mana, character_hp
        else:
            random_num = random.randint(1, 4)
            body_strengthening = random.uniform(1, 2)

            if character_class in ["robber"]:
                mana = character_mana - 50
                match random_num:
                    case 1:
                        return "miss", mana, character_hp
                    case 2:
                        enemy_hp -= ((character_atk * 0.5) * body_strengthening)
                        print(f"You dealt {(character_atk * 0.5) * body_strengthening} damage.")
                        return enemy_hp, mana, character_hp
                    case 3:
                        enemy_hp -= ((character_atk * 1.5) * body_strengthening)
                        print(f"You dealt {(character_atk * 1.5) * body_strengthening} damage.")
                        return enemy_hp, mana, character_hp
                    case 4:
                        enemy_hp -= ((character_atk * 2) * body_strengthening)
                        print(f"You dealt {(character_atk * 2) * body_strengthening} damage.")
                        return enemy_hp, mana, character_hp
            else:
                mana = character_mana - 200
                match random_num:
                    case 1:
                        return "miss", mana, character_hp
                    case 2:
                        enemy_hp -= (character_atk * 1)
                        print(f"You dealt {character_atk * 1} damage.")
                        return enemy_hp, mana, character_hp
                    case 3:
                        enemy_hp -= (character_atk * 2)
                        print(f"You dealt {character_atk * 2} damage.")
                        return enemy_hp, mana, character_hp
                    case 4:
                        enemy_hp -= (character_atk * 2.5)
                        print(f"You dealt {character_atk * 2.5} damage.")
                        return enemy_hp, mana, character_hp

    def damage_absorption(hp, enemy_atk):
        global player_hp

        dodge = random.randint(1, 3)

        if dodge == 1:
            hp -= (enemy_atk * 2)
            print(f"You took double damage. Your remaining HP: {hp}")
            return hp
        elif dodge == 2:
            hp -= enemy_atk
            print(f"You took {enemy_atk} damage. Your remaining HP: {hp}")
            return hp
        elif dodge == 3:
            print("You dodged the attack.")
            return hp

    def save_history(action):
        with open("history.txt", "a") as file:
            file.write(f"{action}\n")

    name, class_character = character()
    player_hp, atk, prot, player_mana = characteristics(class_character)
    enemy_type, enemy_stats = enemy()
    enemy_hp, enemy_atk, enemy_prot = enemy_stats

    print(f"You encountered a {enemy_type} with HP: {enemy_hp}")

    while True:
        action = input("Choose your action (attack / defend / exit): ").lower()
        print(f"Your HP: {player_hp}, Your mana: {player_mana}")

        if action == "exit":
            print("Game over. Goodbye!")
            break
        elif action == "attack":
            result, player_mana, player_hp = character_atk(class_character, atk, player_mana, player_hp, enemy_hp)
            if result == "miss":
                print("Your attack missed!")
            elif result == "invalid":
                print("You cannot attack as a warrior!")
            else:
                absorb_result = damage_absorption(player_hp, enemy_atk)
                print(absorb_result)
            save_history(f"Attacked {enemy_type}")
            if player_hp <= 0:
                print("You have been defeated. Game over.")
                break
            elif enemy_hp <= 0:
                print(f"You defeated the {enemy_type}!")
                enemy_type, enemy_stats = enemy()
                enemy_hp, enemy_atk, enemy_prot = enemy_stats
                print(f"You encountered a {enemy_type} with HP: {enemy_hp}")
        elif action == "defend":
            damage_absorption(player_hp,enemy_atk)
            save_history("Defended")
        else:
            print("Unknown action. Please choose one of the available actions.")


movement()
