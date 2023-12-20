############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
import random
from replit import clear

def game():
  def deal_cards():
    '''Deal 2 cards to player and computer'''
    for i in range(2):
      my_cards.append(random.choice(cards))
      comp_cards.append(random.choice(cards))

  def draw_card(c):
    '''Draw a card'''
    c.append(random.choice(cards))

  def display():
    print(f"Your cards: {my_cards}, current score: {my_score}")
    print(f"Computer's first card: {comp_cards[0]}")

  def keep_score(m, c):
    '''check cards and calc score'''
    ms = 0
    cs = 0
    for card in m:
      ms += card
    for card in c:
      cs += card

    if ms > 21 and 11 in m:
      ace = m.index(11)
      m[ace] = 1
      ms -= 10
    if cs > 21 and 11 in c:
      ace = c.index(11)
      c[ace] = 1
      cs -= 10
      
    return (ms, cs)

  def check_blackjack(c, s):
    if s == 21:
      return True
    else:
      return False


  print(logo)
  my_score = 0
  comp_score = 0
  my_cards=[]
  comp_cards = []
  stop_draw = False
  game_over =  False
  deal_cards()
  (my_score, comp_score) = keep_score(my_cards, comp_cards)

  while not stop_draw:
    display()
    
    if check_blackjack(comp_cards, comp_score):
      print("Game Over, Computer has a blackjack")
      stop_draw = True
      game_over = True
      break
    elif check_blackjack(my_cards, my_score):
      print("Game Over, You win")
      stop_draw = True
      game_over = True
      break
  
    if input("Do you want to draw another card? Type 'y' or 'n':") == 'y' :
      print("You draw a card")
      draw_card(my_cards)
      (my_score, comp_score) = keep_score(my_cards, comp_cards)
      if my_score > 21:
        print("Game Over, You went over.")
        stop_draw = True
        game_over = True
        break
    else:
      while comp_score < 17:
        print(f"Computer's Cards: {comp_cards}")
        print("Computer draws a card")
        draw_card(comp_cards)
        (my_score, comp_score) = keep_score(my_cards, comp_cards)
      stop_draw = True
      
  while not game_over:
    if comp_score > 21 or comp_score < my_score:
      print("Game over, You win")
      game_over = True
    else:
      print("Game over, You lose")
      game_over = True

  if game_over:
    print(f"Your cards: {my_cards}, your score: {my_score}")
    print(f"Computer cards: {comp_cards}, computer score: {comp_score}")
    if input("Do you want to play another game of Blackjack? Type 'y' or 'n': ") == 'y':
      clear()
      game()
    else:
      return

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
  game()

































##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

