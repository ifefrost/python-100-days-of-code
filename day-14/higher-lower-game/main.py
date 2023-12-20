from art import logo, vs
from replit import clear
from game_data import data
import random

def game():

  def check_choice():
    if choice_a['follower_count'] > choice_b['follower_count']:
      return True
    else:
      return False

  
  choice_a = data[random.randint(0, len(data) - 1)]
  def get_choice():
    choice_b = data[random.randint(0, len(data) - 1)]
    while choice_a == choice_b:
      choice_b = data[random.randint(0, len(data) - 1)]
    return choice_b

  choice_b = get_choice()
  score = 0
  in_play = True

  while in_play:
    clear()
    print(logo)

    if score > 0:
      print(f"You're right! Current score: {score}.")
    
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
    print(vs)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_choice == 'A' and check_choice():
      score += 1
    elif user_choice == 'B' and not check_choice():
      score += 1
    else:
      in_play = False
    choice_a = choice_b
    choice_b = get_choice()

  if not in_play:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")

  if input("Would you like to play again? Type 'Y' or 'N': ").upper() == 'Y':
    game()

game()
  
  