import random

def input_multiplication_generator(num1, num2):

    for i in range(1,num2+1):
        
        output = num1 * i

        print(f'{num1} x {i} = {output}')

try:
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    input_multiplication_generator(num1,num2)    
except ValueError:
    print("Number nga lang")