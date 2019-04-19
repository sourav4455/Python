## Program to find factorial of a number given by user

inp = input('Please enter the number to find the factorial of :')

def factorial(inp):
    fact = 1
    for num in range(1,inp + 1):
	fact = fact * num
    print fact

factorial(inp)

