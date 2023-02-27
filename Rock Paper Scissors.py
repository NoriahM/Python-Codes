import random
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

user=int(input("Enter 0 for Rock, 1 for Scissors and 2 for Paper\n"))
computer= random.randint(0,2)
if (user==0):
  print("you chose", rock)
if (user==1):
  print("you chose", scissors)
if (user==2):
  print("you chose", paper)
if (computer==0):
  print("computer chose", rock)
if (computer==1):
  print("computer chose", scissors)
if (computer==2):
  print("computer chose", paper)

if computer==0 and user == 1:
  print("computer Wins!")
if computer==1 and user == 0:
  print("User Wins!")
if computer==1 and user == 2:
  print("computer Wins!")
if computer==2 and user == 1:
  print("User Wins!")
if computer==0 and user == 2:
  print("User Wins!")
if computer==2 and user == 0:
  print("Computer Wins!")
if computer==user:
    print("Draw!!!")


