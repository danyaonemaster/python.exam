import random
def characteristics(class_character):
    match class_character:
        case "magician":
            characteristics_list = [1200, 380, 450, 1200]
            global hp, atk, prot, mana
            hp, atk, prot, mana = characteristics_list
        case "warrior":
            characteristics_list = [1800, 450, 700, 500]
            global hp, atk, prot, mana
            hp, atk, prot, mana = characteristics_list
        case "healer":
            characteristics_list = [1500, 300, 400, 1200]
            global hp, atk, prot, mana
            hp, atk, prot, mana = characteristics_list
        case "robber":
            characteristics_list = [900, 500, 300, 700]
            global hp, atk, prot, mana
            hp, atk, prot, mana = characteristics_list
        case _:
            print("Invalid class")
            character()


def character():
    global name
    name = input("Enter your name: ")
    global class_character
    class_character = input("""Enter your class:
        magician: hp:1200 atk:380 def:450 mana; 1200
        warrior: hp:1800 atk:450 def: 700 mana: 500
        healer: hp:1500 atk: 300 def: 400 mana: 1200
        robber: hp:900 atk: 500 def: 300 mana: 700
        """)
    characteristics(class_character)

def atk(character_atk, enemy_hp):
    atk_Power = character_atk 


character()
