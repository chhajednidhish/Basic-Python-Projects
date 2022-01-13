'''
Design a calculator which will solve all the problems correctly except for 
1. 45*3 = 555
2. 56+9 = 77
3. 56/6 = 4

Your program should take two numbers, operator as input and show the output.
'''

def add(n1,n2):
    ''' To add the given numbers '''
    result = n1+n2
    return result

def sub(n1,n2):
    ''' To subtract given numbers ''' 
    result = n1-n2
    return result

def mul(n1,n2):
    ''' To multiply given numbers '''
    result = n1*n2
    return result

def div(n1,n2):
    ''' To divide the given numbers '''
    result = n1/n2
    return result

def CalculatorLogic(num1,num2,operator):

    # Conditions for calculation including faulty ones
    if(((num1 == 3 and num2 == 45) or (num1 == 45 and num2 == 3)) and operator == '*'): # Faulty condition 1
        print(f"\t\n{num1} * {num2} = 555")
    elif(((num1 == 56 and num2 == 9) or (num1 == 9 and num2 == 56)) and operator == '+'): # Faulty condition 2
        print(f"\t\n{num1} + {num2} = 77")
    elif(((num1 == 56 and num2 == 6) or (num1 == 6 and num2 == 56)) and operator == '/'): # Faulty condition 3
        print(f"\t\n{num1} / {num2} = 4")
    elif(operator == '+'): # If user wants to add numbers
        print(f"\t\n{num1} + {num2} = {add(num1,num2)}")
    elif(operator == '-'): # If user wants to subtract numbers
        print(f"\t\n{num1} - {num2} = {sub(num1,num2)}")
    elif(operator == '*'): # If user wants to multiply numbers
        print(f"\t\n{num1} * {num2} = {mul(num1,num2)}")
    elif(operator == '/'): # If user wants to divide numbers
        print(f"\t\n{num1} / {num2} = {div(num1,num2)}")
    else: 
        print("Invalid Option, please retry")


def main():
    # Introducing the name of app to user
    print("Faulty Calculator".center(40,"-"))

    # Creating looping conditions for using calculator as long as user wants
    cont = 'y'
    while(cont == 'y'):
        # Taking required inputs
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        operator = input("Enter the operator you want to use:")

        # Calling the main logic behind the calculator
        CalculatorLogic(n1,n2,operator)
        cont = str(input("Do you want to continue? y or n? "))
        cont = cont.lower()

    # Thanking user for using our calculator
    print("Thank you for using our calculator!")

if __name__ == "__main__":
    main()