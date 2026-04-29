def print_menu():
    """
    This comment called a docstrings we use it to understand the function.
    print the menu and take a value from user, it is looping if the user don't
    put real value.
    :return: The value from user (1 to 3)
    """
    while True:
        print('\n\nMenu:')
        print('Enter 1 to sum numbers from 1 to N')
        print('Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)')
        print('Enter 3 to end the program')

        user_inp = input('\nEnter choice from 1 to 3: ')

        if user_inp != '1' and user_inp != '2' and user_inp != '3':
            print('Invalid Input...Try again')
            continue
        else:
            return user_inp


def sum_1_to_n():
    """
    This function sum from one to the number as user want, Note: we sum all the
    numbers from one to n except include the n.
    :return: print the total of summation.
    """
    n = int(input("Enter a number: "))
    sum_all = (n * (n - 1)) // 2
    print("Sum from 1 to", n, "is", sum_all)


def divide(num1, num2, operation):
    """
    Perform a division operation between two numbers.
    Parameters:
        num1 (int or float): The numerator (the number to be divided).
        num2 (int or float): The denominator (the number to divide by).
        operation (str): The type of division to perform.
                         "/"  -> true division (returns float result)
                         "//" -> floor division (returns integer result)
    Returns:
        int or float: The result of the division if valid.
        None: If division by zero occurs or operation is invalid.
    Notes:
        - Division by zero is not allowed.
        - If an unsupported operation is provided, the function returns None.
    """
    if num2 == 0:
        result = None
    elif operation == "/":
        result = num1 / num2
    elif operation == "//":
        result = num1 // num2
    else:
        result = None
    return result


def expression():
    """
       Prompts the user to enter a simple mathematical expression,
       evaluates it, and prints the result.
       The input should be in the format:
           <number> <operation> <number>
       Example:
           5 + 3
       Supported operations:
           +   : addition
           -   : subtraction
           *   : multiplication
           **  : exponentiation
           /   : division (handled by divide function)
           //  : floor division (handled by divide function)
       The function converts input numbers to float, performs the
       requested operation, and prints the result.
       If the operation is division and the second number is zero,
       the divide function handles the error and returns None.
       :return: None
       """
    num1, operation, num2 = input('Enter a simple expression: ').split()
    num1, num2 = float(num1), float(num2)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '**':
        result = num1 ** num2
    else:
        result = divide(num1, num2, operation)
    if result != None:
        print('Expression value is ', result)
    else:
        print('Sorry: No way to compute this expression')


def calculator_interface():
    """
        Provides a simple command-line interface for the calculator program.
        This function runs in an infinite loop, displaying a menu to the user
        and executing the selected option.
        Menu options:
            '1' : Calls sum_1_to_n() to calculate the sum from 1 to N
            '2' : Calls expression() to evaluate a mathematical expression
            Any other input : Exits the program
        The loop continues until the user chooses to exit.
        :return: None
        """
    while True:
        user_inp = print_menu()

        if user_inp == '1':
            sum_1_to_n()
        elif user_inp == '2':
            expression()
        else:
            break
calculator_interface()
