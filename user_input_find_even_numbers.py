## Take any input from user. Run the loop that many time and print all the even numbers in between

inp = input("Please enter any number :")

for num in range(inp)[1:]:
    if num % 2 == 0:
        print num

