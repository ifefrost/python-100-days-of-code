from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
auction = {}
add_new = True
while add_new:
  name =  input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  
  auction[name] = bid
  next = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if next == 'yes':
    clear()
  elif next == 'no':
    clear()
    add_new = False

winner = ''
winner_bid = 0
for key in auction:
  if auction[key] > winner_bid:
    winner_bid = auction[key]
    winner = key

print(f"The winner is {winner} with a bid of ${winner_bid}")