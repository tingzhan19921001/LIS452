##part 1
import random
guesstime1 = 0
minimum = 0
maximum = 100
number = random.randint(1,100)
print('I am thinking of a mumber between 1 and 100')
while True:
    

    guess = int(input('Guess'))

    if minimum <= guess <= maximum:## i add this because I want to prevent intentionl wrong guessing
        guesstime1 = guesstime1 + 1
        if guess == number:
            print('congratulations,you have done great!')
            break
 

        elif guess < number:
            print('Your guess is too low, guess again.')
            minimum = guess 

        elif guess > number:
            print(' Your guess is too high, guess again.')
            maximum = guess 

    else:##prevent if one tries to increase the guessetime by guessing wrong numbers on purpose, and this intentional wrong guessing will not be counted
        print('Out of range,guess again.')
        continue
    
 
print('Your guesstime is,' , guesstime1, ',Hope to see you soon.')
print()
print()
##Part 2 
import random
print('Game time!')
print('If the guess is lower than the chosen number, type l/L(Low); if the guess is greater than the chosen number, type h/H(High); if the guess is equal to the chosen number, type c/C(Correct).') 
minimum = 0
maximum = 100
guesstime2 = 0
number = int(input('Choose a number:'))
print('I have chosen',number,', I am ready to begin.')
while True:
    guess = random.randint(minimum,maximum)
    print(guess)
    
    command = input('Type your response')

    guesstime2 = guesstime2 + 1
    if command in ['c','C']:
            print('Congratulations, you have done great!')
            break


    elif command in ['l','L']:
            print('Your guess is too low,guess again.')
            minimum = guess + 1

    elif command in ['h', 'H']:
        print('Your guess is',guess,'.Your guess is too high, guess again.')
        maximum = guess-1


print('Your guesstime is', guesstime2, ',congratulations!')
print()
print()
if guesstime1 > guesstime2:
    print('Computer Win.')
if guesstime1 < guesstime2:
    print('Human Win.')
if guesstime1 == guesstime2:
    print('Even.')
          
