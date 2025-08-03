x = float(input("enter the first number: "))
y = float(input("enter the second number: "))

operation = str(input("the operaion '-' for substraction, '+' for adition, '*' for multiplication and '/' for division") )

if operation == '+':
    print(f"Addition : {x} + {y} = {x+y}")
elif operation == '-':
    print(f"soustraction : {x} - {y} = {x-y}")
elif operation == '*':
    print(f"multiplication : {x} * {y} = {x*y}")
elif operation == '/':
    if y == 0:
        print("Impossible calculation")
    else:
        print(f"division : {x} / {y} = {x/y}")
else :
    print ("Invalid enter")