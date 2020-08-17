# Guess the Number
import time
import random

print("Hello there! What is your name?")
name = input()
print("Well, " + name + ". I'm thinking of a number between 1 and 10.")
time.sleep(2)
print("Can you guess what number I'm thinking of?")
secretNumber = random.randint(1, 10)
time.sleep(2)
print("I'll give you five tries.")
time.sleep(2)
print("Take a guess...")

for guessesTaken in range(1, 6):
    global guess
    guess = int(input())
    if guess < secretNumber:
        print("Too low. Guess a little higher.\n")
    elif guess > secretNumber:
        print("Too high. Guess a little lower.\n")
    else:
        break

if guess == secretNumber:
    print("Congrats, " + name + "! You got it!")
    time.sleep(2)
    print("And it took you " + str(guessesTaken) + " guesses.")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
    time.sleep(2)
    print("Try again later")
