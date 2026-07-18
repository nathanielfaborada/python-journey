def prime_checker(num1):
    is_prime = True

    for i in range(2, num1):        
        if num1 % i == 0 :
            output = num1 // i
            is_prime = False 
            break

    if is_prime:
        print(f'{num1} % is prime')
    else:
        print(f'{num1} % {i} = {num1 % i} Exactly')
        print(f'{num1} is composite, divisible by {i} ({num1} = {i} x {output})')

while True:
    
    try:
        num1 =  int(input("Enter a number to know if that prime or composite = "))
        prime_checker(num1)
        break

    except ValueError:
        print("Enter a number not a character")
