# This is a guess the number game.
import random
secretNumber = random.randint(1, 30)
print('I am thinking of a number between 1 and 30.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Whats your guess?.')
    guess = int(input())

    if guess < secretNumber:
        print('Too Low, Try again!')
    elif guess > secretNumber:
        print('Too high, Try again.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Great job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry, You lost the Guess Game. The number I was thinking of was ' + str(secretNumber))
