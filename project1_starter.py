"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Daylen Hicks]
Date: [10/28/2025]

AI Usage: ChatGPT assisted with writing file-handling logic for saving and loading data.
- ChatGPT helped structure functions and connect program sections logically.
- ChatGPT reviewed code comments and suggested clear documentation practices.
"""
#

import random
import os

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    level = 1
    
    strength, magic, health = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 200
    }
    
    return character

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
# TODO: Implement this function
    if character_class == "Warrior":
        base_str, base_mag, base_hp = 10, 3, 150
        growth_str, growth_mag, growth_hp = 3, 1, 20
    elif character_class == "Mage":
        base_str, base_mag, base_hp = 5, 12, 90
        growth_str, growth_mag, growth_hp = 1, 4, 10
    elif character_class == "Rogue":
        base_str, base_mag, base_hp = 7, 7, 80
        growth_str, growth_mag, growth_hp = 2, 2, 8
    elif character_class == "Cleric":
        base_str, base_mag, base_hp = 6, 10, 120
        growth_str, growth_mag, growth_hp = 2, 3, 15
    else:
        base_str, base_mag, base_hp = 5, 5, 70
        growth_str, growth_mag, growth_hp = 1, 1, 5

    # Calculate stats for current level
    strength = base_str + (level - 1) * growth_str
    magic    = base_mag + (level - 1) * growth_mag
    health   = base_hp  + (level - 1) * growth_hp

    # Add small random bonus only if level > 1
    if level > 1:
        strength += random.randint(0, 3)
        magic += random.randint(0, 3)
        health += random.randint(0, 5)

    return (strength, magic, health)


def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """

    # TODO: Implement this function
    # Remember to handle file errors gracefully
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        # Directory does not exist
        return False
    
    f = open(filename, "w")
    f.write(f"Character Name: {character['name']}\n")
    f.write(f"Class: {character['class']}\n")
    f.write(f"Level: {character['level']}\n")
    f.write(f"Strength: {character['strength']}\n")
    f.write(f"Magic: {character['magic']}\n")
    f.write(f"Health: {character['health']}\n")
    f.write(f"Gold: {character['gold']}\n")
    f.close()
    return True

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    if not os.path.exists(filename):
        return None
    f  = open(filename, "r")
    lines = f.readlines()
    
    character_data = {}
    for line in lines:
        key, value = line.strip().split(": ")
        if key == "Character Name":
            character_data["name"] = value
        elif key == "Class":
            character_data["class"] = value
        elif key == "Level":
            character_data["level"] = int(value)
        elif key == "Strength":
            character_data["strength"] = int(value)
        elif key == "Magic":
            character_data["magic"] = int(value)
        elif key == "Health":
            character_data["health"] = int(value)
        elif key == "Gold":
            character_data["gold"] = int(value)
    f.close()
    return character_data



def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    character["level"] += 1
    # Recalculate stats using calculate_stats()
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50
    print(f"\n🎉 {character['name']} leveled up to Level {character['level']}!")

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    name = input("Enter your character's name: ")
    cclass = input("Choose class (Warrior/Mage/Rogue/Cleric): ")

    hero = create_character(name, cclass)
    display_character(hero)

    save_character(hero, f"{hero['name'].lower()}.txt")
    print("\nCharacter saved successfully!")

    level_up(hero)
    display_character(hero)

    # Load character example
    loaded_hero = load_character(f"{hero['name'].lower()}.txt")
    if loaded_hero:
        print("\nCharacter loaded from file:")
        display_character(loaded_hero)
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
