from art import logo

print(logo)

def add(n1, n2):
  '''Add two numbers together'''
  return n1 + n2

def subtract(n1, n2):
  '''Subtract a number from a first number'''
  return n1 - n2

def multiply(n1, n2):
  '''Multiply two numbers together'''
  return n1 * n2

def divide(n1, n2):
  '''Divide a number by a second number'''
  return n1 / n2

operations = {'+':add, '-': subtract, '*':multiply, '/':divide}

first = int(input("What's the first number?: "))
for key in operations:
  print(key)
operation = input("Pick an operation: ")
second = int(input("What's the second number?: "))
function = operations[operation]
answer = function(first, second)

print(f"{first} {operation} {second} = {answer}")