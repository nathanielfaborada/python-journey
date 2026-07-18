
def even_odd_checker():


    for i in range(1,100):
        
        output = i % 2 == 0

        if output:
            print(f'{i} is even')
        else:
            print(f'{i} is odd')

even_odd_checker()