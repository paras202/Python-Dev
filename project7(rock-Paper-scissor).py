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
choices = [rock , paper , scissors]
user_choice = int(input("what do you choose?\nType 0 for Rock , 1 for Paper , 2 for Scissors||\n"))
while user_choice > 2 or user_choice < 0:
  print("invalid choice!")
  user_choice = int(input("choose again....\n"))
#else:
computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}.")
print("________________________________________________________________________________________")
print(choices[user_choice])
print("________________________________________________________________________________________")
print(choices[computer_choice])
print("________________________________________________________________________________________")
if user_choice == 0 and computer_choice == 2:
  print("You Win!")
elif computer_choice == 0 and user_choice == 2:
  print("You Lose!......\n\n\n**************************************GAME OVER!****************************************")
elif computer_choice > user_choice:
  print("You Lose!......\n\n\n**************************************GAME OVER!****************************************")
elif user_choice > computer_choice:
  print("You Win!")
elif computer_choice == user_choice:
  print("It's a draw......\n\n\n**************************************GAME OVER!****************************************")
else:
  print("Illegal move......\n\n\n**************************************GAME OVER!****************************************")