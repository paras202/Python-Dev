print("designing a BMI index\n")
height = float(input("enter your height in meters = "))
weight = float(input("enter your weight in kg = "))
bmi = weight/(height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi} , you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi} , you have a normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi} , you are slightly overweight")
else:
    print(f"your bmi is {bmi} , you are obese")
