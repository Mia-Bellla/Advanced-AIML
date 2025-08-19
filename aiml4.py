
import random

print("Welcome to Random Library")

# User enters items (comma-separated)
items = input("Enter some items separated by commas: ").split(",")

# Clean up extra spaces
items = [i.strip() for i in items if i.strip()]

if not items:
    print("Invalid Entry")
else :

    # Random choice
    print("Random pick:", random.choice(items))

    # Random shuffle
    random.shuffle(items)
    print("Shuffled order:", items)

    # Random sample
    if len(items) >= 2:
        print("Random sample of 2:", random.sample(items, 2))

    # Random number demo
    print("Lucky number between 1–100:", random.randint(1, 100))
