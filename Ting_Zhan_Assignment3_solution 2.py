##part 1
##in this solution, I remove the limits that helps to prevent intentional wrong guessing
import random
guesstime1 = 0
number = random.randint(1,100)
print('I am thinking of a mumber between 1 and 100')
while True:
    

    guess = int(input('Guess'))

    guesstime1 = guesstime1 + 1
    if guess == number:
        print('congratulations,you have done great!')
        break
 

    elif guess < number:
        print('Your guess is too low, guess again.')
       

    elif guess > number:
        print(' Your guess is too high, guess again.')
      

 
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

    
    if command in ['c','C']:
            guesstime2 = guesstime2 + 1
            print('Congratulations, you have done great!')
            break


    elif command in ['l','L']:
            print('Your guess is too low,guess again.')
            minimum = guess + 1

    elif command in ['h', 'H']:
        print('Your guess is',guess,'.Your guess is too high, guess again.')
        maximum = guess-1

    else:##if there is wrong input then it should not be counted how to realize it?
        print('Wrong input')


print('Your guesstime is', guesstime2, ',congratulations!')
print()
print()
if guesstime1 > guesstime2:
    print('Computer Win.')
if guesstime1 < guesstime2:
    print('Human Win.')
if guesstime1 == guesstime2:
    print('Even.')
          
