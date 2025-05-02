import random

barril=random.randint(1,6)
rul=int(input("dispare: "))
while rul!=barril:
    rul=int(input("dispare: "))
print("BANG!!!")