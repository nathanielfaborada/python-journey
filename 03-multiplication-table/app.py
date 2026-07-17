def multiplication_generator():

    table_list = [1,2,3,4,5,6,7,8,9,10]

    print("-"*100)
    print("Table 1 to 5") 
    print()
    for i in range(0, 11):
        output1 = table_list[0] * i
        output2 = table_list[1] * i
        output3 = table_list[2] * i
        output4 = table_list[3] * i
        output5 = table_list[4] * i

        print(f'{table_list[0]} x {i} = {output1}', end='\t')
        print(f'{table_list[1]} x {i} = {output2}', end='\t')
        print(f'{table_list[2]} x {i} = {output3}', end='\t')
        print(f'{table_list[3]} x {i} = {output4}', end='\t')
        print(f'{table_list[4]} x {i} = {output5}')


    print("-"*100)
    print("Table 6 to 10")
    print()
    for i in range(0,11):

        
        output6 = table_list[5] * i
        output7 = table_list[6] * i
        output8 = table_list[7] * i
        output9 = table_list[8] * i
        output10 = table_list[9] * i
        
        print(f'{table_list[5]} x {i} = {output6}', end='\t')
        print(f'{table_list[6]} x {i} = {output7}', end='\t')
        print(f'{table_list[7]} x {i} = {output8}', end='\t')
        print(f'{table_list[8]} x {i} = {output9}', end='\t')
        print(f'{table_list[9]} x {i} = {output10}')
        
multiplication_generator()
