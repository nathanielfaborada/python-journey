def even_odd_checker(num1):
    output = num1 % 2 == 0
    if output:
        print(f'{num1} is even')
    else:
        print(f'{num1} is odd')


while True:
    
    try:
        num1 =  int(input("Enter a number to know if that odd or even = "))
        even_odd_checker(num1)
        break

    except ValueError:
        print("Enter a number not a character")
