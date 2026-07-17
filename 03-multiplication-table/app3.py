
def print_table_group(numbers, i):
    for num in numbers:
        output = num * i
        print(f'{num} x {i} = {output}', end='\t')
    print()

def multiplication_generator():

    table_list = list(range(1, 101))

    print("-"*100)
    print("Table 1 to 5") 
    print()
    for i in range(0, 11):
        print_table_group(table_list[0:5],i)

    print("-" * 100)
    print("Table 6 to 10")
    print()
    for i in range(0, 11):
        print_table_group(table_list[5:10], i)
        
multiplication_generator()