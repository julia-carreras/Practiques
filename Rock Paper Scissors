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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print (paper)
elif user_choice == 2:
    print (scissors)
else:
    print("You typed an invalid number, you lose!")
    quit()

print("Computer chose:")

import random
options = [rock, paper, scissors]
computer_choice = random.randint(0,2)
print(options[computer_choice])

if user_choice == computer_choice:
    print("It's a draw")

elif ((user_choice == 2 and computer_choice == 0 or
user_choice == 1 and computer_choice == 2 or
user_choice == 0 and computer_choice == 1)):
    print("You lost")

else:
    print("You win")
