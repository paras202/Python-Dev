print('''  MAKING A CALCULATOR USING PYTHON ''')
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
# operation = input("Op:")
# c = int(input("a: "))
# d = int(input("b: "))
# def calculator(op, a, b):
#     if op == "+":
#         return a+b
#     elif op == "-":
#         return a-b
#     elif op == "*":
#         return a*b
#     elif op == "/":
#         return a/b
# print(calculator(operation,c,d))
def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def product(a, b):
    return a*b
def divide(a, b):
    return a/b
def exponent(a, b):
    a = int(a)
    b = int(b)
    return a**b
def remainder(a, b):
    return a%b
def div_int(a, b):
    return a//b
calci = {
  '+': add,
  '-': subtract,
  '*': product,
  '/': divide,
  '^': exponent,
  '%': remainder,
  '//': div_int,
}
def calculator():
    c = float(input("a: "))
    should_continue = True
    while should_continue:
        operation = input("Op:")
        d = float(input("b: "))
        perform = calci[operation]
        answer = perform(c, d)
        print(answer)
        a = input(f" type 'yes' to continue with {answer}.\n    Or    \n'new' to continue with new value.\n    Or     \n'exit':")
        if a == "yes":
            c = answer
        elif a == "exit":
            break
        elif a == "new":
            should_continue = False
            calculator()
        else:
            return "invalid input"
calculator()
# '''____________________________________________________________type 2_______________________________________________________'''
