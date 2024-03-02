#project making hangman game from python of choosing a random word and guess every time
import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = [''' 
 +----+
 |    |
 O    |
/|\   |
/ \   |
      |
=========
''', ''' 
 +----+
 |    |
 O    |
/|\   |
/     |
      |
=========
''', ''' 
 +----+
 |    |
 O    |
/|\   |
      |
      |
=========
''',''' 
 +----+
 |    |
 O    |
/|    |
      |
      |
=========
''', ''' 
 +----+
 |    |
 O    |
 |    |
      |
      |
=========
''', ''' 
 +----+
 |    |
 O    |
      |
      |
      |
=========
''']
#update the word list to use the 'word list' from hangman_words.py
# word_list = ["aardvark", "baboon", "camel", "paras", "mayank", "jasmehar"]
from hangman_words import word_list
chosen_word = random.choice(word_list)
lives = len(stages)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display = []
n = len(chosen_word)
#create list display with "_"
for i in range(0,n):
  display.append("_")
print(display)
#create a boolean end of game = true / false 
end_of_game = False
#start with while loop as negation of boolean word
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  #match the guess word from all the alphabets in chosen word
  if guess in display:
    print(f"You've already guessed the letter {guess}")
  for i in range(0,n):
    letter = chosen_word[i]
    if letter == guess:
      display[i] = letter
  #decrease lives for a wrong guess
  if guess not in chosen_word:
    print(f"You've guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    print(stages[lives])

    #at all lives are lost make bool end of game true and print YOU LOOSE
    if lives == 0:
      end_of_game = True
      print("YOU LOOSE")
    #to convert list in string we use join 
  print(f"{' '.join(display)}")
  #check for winning condition
  if "_" not in display:
    end_of_game = True
    print("YOU WIN")
  