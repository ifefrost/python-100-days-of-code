rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player_choice = int(input())
computer_choice = random.randint(0,2)
choices = [rock, paper, scissors]
print(f"You chose {choices[player_choice]}")
print(f"Computer chose {choices[computer_choice]}")
if(player_choice == computer_choice):
  print("It's a tie!")
elif(computer_choice == 0 and player_choice == 2):
  print("You lose!")
elif((player_choice == 0 and computer_choice == 2) or (player_choice > computer_choice)):
  print("You win!")
else:
  print("You lose!")
