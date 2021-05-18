import random

print("What's your name?")
name = input()

print("Hi " + name + ", I have a number between 1 and 20 and you need to guess it. You have 6 attempts.")
number = random.randint(1,20)

for guesses in range(1, 7):
    print("What's your guess?")
    yourguess = int(input())
    
    if yourguess < number:
        print("Your guess is too low.")
    elif yourguess > number:
        print("Your guess is too high.")
    else:
        break
    
if yourguess == number:
    print("Well done " + name + ". You guessed the number in " + str(guesses) + " guesses.")
else:
    print("Game Over. My number was " + str(number))
