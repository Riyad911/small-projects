#Design a small application that keeps asking the user 3 choices:
#Enter 1 to sum integers from 1 to N
#Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)
#Expect 3 items. Operations are: + - * / // **
#Enter 3 to end the program
#The user should input value from 1 to 3
#Otherwise, inform that this is invalid and try again
#Take proper input from the
from itertools import count
from os.path import split

flag = True
while flag:
    num = int(input('''
Menu:
1 to sum integers from 1 to N
2 to evaluate simple 2 numbers expression (e.g. 2 + 3)
3 to end the program 
Enter choice from 1 to 3 -->>: '''))
    if num == 3:
        flag = False
    elif num == 2:
        num1, operation, num2 = input("Enter a simple expression: ").split()
        num1, num2 = float(num1), float(num2)
        if operation == '+':
            print("Expression value is:", num1 + num2)
        elif operation == '-':
            print("Expression value is:", num1 - num2)
        elif operation == '*':
            print("Expression value is:", num1 * num2)
        elif operation == '**':
            print("Expression value is:", pow(num1, num2))
        else:
            if num2 == 0:
                print('Sorry: No way to compute this expression')
            elif  operation == '/':
                print("Expression value is:", num1 / num2)
            elif operation == '//':
                print("Expression value is:", num1 // num2)
    elif num == 1:
        value = int(input("Enter a number: "))
        sum_num = 0
        copy_value = value
        while value >= 1:
            sum_num += value
            value -= 1
        print("Sum from 1 to",copy_value,"is", sum_num)
    else:
        print("Invalid Input...Try again")


