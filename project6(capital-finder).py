states_india = ["rajasthan" , "punjab" , "haryana" , "himachal pradesh" , "bihar" , "kerala" , "west bengal" , "UP" , "manipur" , "utarakhand" , "karnataka" , "Goa" , "gujarat" , "madhya pradesh" , "jharkhand" , "tamil nadu" , "andhra pradesh" , "telangana" , "arunachal pradesh" , "assam" , "maharashtara" , "tripura" , "sikkim" , "meghalaya" , "Nagaland" , "orissa" , "mizoram" , "chhattisgarh"]
capital = ["jaipur" , "chandigarh" , "chandigarh" , "shimla" , "patna" , "thiruvananthapuram" , "kolkata" , "lucknow" , "imphal" , "dehradun" , "bengaluru" , "panji" , "gandhinagar" , "bhopal" , "ranchi" , "chennai" , "hyderabad" , "hyderabad" , "ittanagar" , "dispur" , "mumbai" , "agartala" , "gangtok" , "shillong" , "kohima" , "bhuvaneshwar" , "aizwal" , "raipur" ]
india = [states_india , capital]
# states_no = len(states_india)
#print(len(capital))
print(states_india)
n = int(input("no of state you want to know the capital! \n"))
print(india[1][n]  + "is a capital of the state "  + india[0][n])
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])
# print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])