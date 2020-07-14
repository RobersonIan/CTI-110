# CTI-110
# P3HW2 - BasicMath
# Ian Roberson
# 6/30/2020


##variables
##n = True ----For the while statement
##
##input
##
##num1 = user's input
##num2 = user's input
##action = user's input -------choses the operator that will be used
##
##calculations
##if action = 1 --- add
##if action = 2 --- multiply
##if action = 3 --- subtract
##if action = 4 --- exit program by setting n equal to false
##else error


def calculations(num1, num2):
    action = int(input('Select option: '))
    if action == 1:
        print(num1, '+', num2, '=', num1 + num2)
    elif action == 2:
        print(num1, '*', num2, '=', num1 * num2)
    elif action == 3:
        print(num1, '-', num2, '=', num1 - num2)
    elif action == 4:
        print('Exiting program')
        n = False
    else:
        print()
        print()
        print('Error: invalid selection')
        print()
        print()
        print('First number is:', num1)
        print('Second number is:', num2)
        print('-----------MENU---------------')
        print('        1) Add Numbers')
        print('        2) Multiply Numbers')
        print('        3) Subtract Numbers')
        print('        4) Exit')
        print('------------------------------')
        calculations(num1, num2)
    return


n = True
while n == True:

    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    
    print('-----------MENU---------------')
    print('        1) Add Numbers')
    print('        2) Multiply Numbers')
    print('        3) Subtract Numbers')
    print('        4) Exit')
    print('------------------------------')

    #action = float(input('Select option: '))
    calculations(num1, num2)
