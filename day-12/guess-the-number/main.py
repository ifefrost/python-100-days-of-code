#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
import random

def game():
  def setDifficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
      return 10
    elif difficulty == "hard":
      return 5
    else:
      print("Invalid difficulty. Try again.")
      return setDifficulty()
  
  def checkGuess(g):
    if g < answer:
      print("Too low.")
    elif g > answer:
      print("Too high.")
    elif g == answer:
      print(f"You got it! The answer was {answer}.")
      return True
    else:
      print("Invalid guess. Try again.")
    return False

  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  turns = setDifficulty()
  answer = random.randint(1, 100)

  while turns > 0:
    print(f"You have {turns} attempts remaining.")
    guess = int(input("Make a guess: "))
    if checkGuess(guess):
      break
    turns -= 1
  if turns == 0:
    print(f"You've run out of turns. The answer was {answer}. You lose!")

  playAgain = input("Would you like to play again? Type 'y' or 'n': ").lower()
  if playAgain == "y":
    clear()
    game()
  else:
    print("Closing, Goodbye!")
    exit()

game()


# print(logo)
# print("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100.")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# turns = 0
# if difficulty == "easy":
#     turns = 10
# elif difficulty == "hard":
#     turns = 5
# else:
#     print("Please choose a valid difficulty.")
#     exit()
# answer =  random.choice(range(2,100))
# guess = 0
# while turns > 0:
#   print(f"You have {turns} attempts remaining to guess the number.")
#   guess = int(input("Make a guess: "))
#   if guess < answer:
#     print("Too low.\nGuess Again")
#     turns -= 1
#   elif guess > answer:
#     print("Too high.\nGuess Again")
#     turns -= 1
#   elif guess == answer:
#     print(f"You got it! The answer was {answer}.")
#     break
#   else:
#     print("Please enter a valid number.")
#     exit()

# if turns == 0:
#   print(f"You ran out of turns. The answer was {answer}. You lose!")
    