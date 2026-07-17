def input_multiplication_generator(num1, num2):

    for i in range(1,num2+1):
        
        output = num1 * i

        print(f'{num1} x {i} = {output}')

try:
    num1 = int(input("Enter a number: ")) 
    num2 = int(input("Up to what number? "))
    input_multiplication_generator(num1,num2)    
except ValueError:
    print("Number nga lang")
