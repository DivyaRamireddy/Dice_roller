import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Welcome to Dice Roller!")
    while True:
        choice = input("\nPress ENTER to roll the dice (or type 'q' to quit): ")
        if choice.lower() == 'q':
            print("👋 Goodbye!")
            break
        result = roll_dice()
        print(f"✅ You rolled: {result}")

if __name__ == "__main__":
    main()
