import random

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number bertween 1 and 100")
number=random.randint(1,100)
guess=67
num_guesses=0
while guess !=number:
 guess=int(input("Guess the number:"))

 if guess<number:
  print("Too low,try again")
 elif guess>number:
  print("Too high,try again")
 else:
  print (f"Congratulations! You guess the number in guess:")