import random

print("welcome to the random item picker! seperate items by a space!")
items = input("Items to choose from: ")
list = items.split()
print("--------------------------------")
print("Picked: " + random.choice(list))
print("--------------------------------")

