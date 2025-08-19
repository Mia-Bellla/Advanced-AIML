from art import *

print("Welcome to Art Library \n")

# 1. Generate art text
print("Text in different styles:")
print(text2art("HELLO"))        # Default style
print(text2art("Love", font="block"))
print(text2art("Python", font="random"))

# 2. Random ASCII art
print("\nRandom ASCII art:")
print(art("random"))

# 3. Some predefined art
print("\nCute animals:")
print(art("butterfly"))
print(art("cat"))
print(art("fish"))

# 4. Emoji-like art
print("\nFun emoji-style art:")
print(art("happy"))
print(art("kiss"))
print(art("heart"))
