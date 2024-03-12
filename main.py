import random
from art import logo
from replit import clear

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

rand_value = random.randint(1, 100)
print(f"It's the answer:)  = {rand_value}")

attempts = 5


def make_choice():
 
  """If the user chooses the 'easy' difficulty level, it adds 5 to the attempts variable and returns this value. In other words, if the user selects 'easy', the total number of attempts increases by 5."""

  """If the user chooses the 'hard' difficulty level, it adds 10 to the attempts variable and returns this value"""

  choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  if choice == 'easy':
    return attempts + 5
    
  elif choice == 'hard':
    return attempts
  else:
    print("Invalid choice")
    return make_choice()

#Assign the value to the attempts variable by calling the make_choice function.
attempts = make_choice()



#when the number of attempts is 0, the game is over
#when the number is guessed, the game is over
def make_guess(attempts):

  should_continue = True
  while should_continue:
    if attempts > 0:
      if should_continue:
        #the attempts variable is updated based on the difficulty level selected by the user.
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        
        if guess < rand_value:
          print("Too low.\nGuess again.")
    
        elif guess > rand_value:
          print("Too high.\nGuess again.")
    
        else:
          print(f"\nYou got it! The answer was {rand_value}.")
          should_continue = False

    
        
    elif attempts == 0:
      print(f"\nYou've run out of guesses, The answer was {rand_value}.")
      should_continue = False


    
make_guess(attempts)


