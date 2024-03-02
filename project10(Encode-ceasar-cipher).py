logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(given_text,shift_n,c_direction):
  end_text = ""
  if c_direction == "decode":
    shift_n *= -1
  for letter in given_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_n
      if new_position >= 26:
        new_position -= 26  
      elif new_position < 0:
        new_position += 26
      end_text += alphabet[new_position]
    else:
       end_text += letter
  print(f"The {c_direction}d text is {end_text}")
should_end = False
while not should_end:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(given_text=text,shift_n=shift,c_direction=direction)
  t = input("(Type 'Yes' to contiue or 'No' to end the ceaser cipher):\n").lower()
  if t == 'no':
    should_end == True
    print("Goodbye")

# def encrypt(o_text,shift_n):
#   new_text = ""
#   for letter in o_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_n
#     if new_position >= 26:
#       new_position -= 26
#       new_text += alphabet[new_position]
#     else:
#       new_text += alphabet[new_position]
#   print(f"The encoded text is {new_text}.")
# def decrypt(given_text,shift_nu):
#   old_text = ""
#   for letter in given_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_nu
#     if new_position < 0:
#       new_position += 26 
#       old_text += alphabet[new_position]
#     else:
#       old_text += alphabet[new_position]
#   print(f"The decoded text is {old_text}.")
# #function call
# if direction == "encode":
#   encrypt(o_text=text, shift_n=shift)
# elif direction == "decode":
#   decrypt(given_text=text,shift_nu=shift)