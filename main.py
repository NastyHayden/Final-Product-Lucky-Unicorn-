import time

import os

print("Press <enter> to play")
enter = input()



if enter == "":
  print("Booting system...")

  print()

  time.sleep(1.3)

  import random

  error_chance = random.randint(1, 20)

  if 1 <= error_chance <= 5:
    print("system error please try again")
    time.sleep(2)
    
    os.system('clear')
    
    print("Lets try this again")

    print()


    print("Press enter to play")
    
    enter = input()

    print("Booting system...")
    
    time.sleep(3)

    print()

    print("Succesfully booted")
    print()



   
  else:
    print("Succesfully booted")
    print()
  

 

def statement_generator(statement, decoration):

  sides = decoration * 3

  statement = "{} {} {}".format(sides, statement,sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""



statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()



def yes_no(question):  
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "yes" or response == "y":
      response == "yes"
      return response

    elif response == "no" or response == "n":
      response == "no"
      return response

    else:
      print("Please answer yes / no")


def instructions():
  print()
  print("**** How To Play ****")
  print()
  print("Ok here are the rules. You will pay $1 per round, Every round you will type 'Enter' and a random token will be generated If the token is a unicorn you win $4 if it is a zebra or horse you lose 0.50c and if it is a donkey then you don’t win anything")
  time.sleep(15)
  os.system('clear')
  
  return ""

def num_check(question, low, high):
  error = "Please enter an whole number between 1 and 10"

  valid = False
  while not valid:
    try:

      response = int(input(question))

      if low < response <= high:
        return response 
        

      else:
        print(error)

    except ValueError:
      print(error)


# Main routine goes here...

played_before = yes_no("Have you played the game before? ")

if played_before == "no" or played_before == "n":
  instructions()

print()

how_much = num_check("How much would you ""like to play with? ", 0, 10)


# Main routine go here

import random


balance = how_much

rounds_played = 0

print()
print("Your starting balance is $" + str(balance))
print()
play_again = input("Press <Enter> to play... ").lower()

while play_again == "":
  rounds_played += 1


  print()
  print("*** Round #{} ***".format(rounds_played))

  
  chosen_num = random.randint(1,100)

  if 1 <= chosen_num <= 5:
    chosen = "unicorn"
    balance +=4

  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    balance -= 0.5 
   
  else:
   if chosen_num % 2 == 0:
     chosen = "horse"
   else:
     chosen = "zebra"
  balance -= 0.5

  print ("you got a " + (chosen) + ". Your balance is $" + str(balance))
  if balance < 1: 
    play_again = "xxx"
    print("Sorry you have run out of money")
  else:
    play_again = input("Press Enter to play again ""or type any key to quit ")
  
print ()
print("Your final balance is", balance)
