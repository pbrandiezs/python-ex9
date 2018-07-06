import random

a = random.randint(1, 9)
print(str(a))

guess = int(input("Enter your guess? "))
if guess < a:
    print("Your guess is too low! ")
if guess > a:
    print("Your guess is too high! ")
if guess == a:
    print("Your guess is correct!! ")

