import random

a = ["heads", "tails"]
b = random.choice(a)

user = input("Heads or tails? \n")

print("You chose",  user, "and we got a " + b + "!")