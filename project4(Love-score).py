print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
both_name = name1 + name2
small_name = both_name.lower()
T = small_name.count("t")
R = small_name.count("r")
U = small_name.count("u")
E = small_name.count("e")
true = T + R + U + E
L = small_name.count("l")
O = small_name.count("o")
V = small_name.count("v")
E = small_name.count("e")
love = L + O + V + E 
love_score = int(str(true) + str(love))
if (love_score < 10 ) or (love_score > 90 ):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
if (love_score >= 40 ) and (love_score <= 50 ):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"your score is {love_score}.")