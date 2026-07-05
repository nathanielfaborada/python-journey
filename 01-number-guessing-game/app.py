import random
import os

guess_number_easy = random.randint(1,10)
counter_number_easy = random.randint(1,6)

guess_number_medium = random.randint(1,30)
counter_number_medium = random.randint(1,4)

guess_number_hard = random.randint(1,50)
counter_number_hard = random.randint(1,2)





while True:
    print("Do you want to play?")
    print("Choose difficulty")
    print("Enter 1 for Easy")
    print("Enter 2 for Medium") 
    print("Enter 3 For Hard")

    choice = int(input("Pick your choice"))
    counter = 0
    
    if choice == 1:
        print("Can you guess the number")
        print("The system gives you", counter_number_easy)

        while True:
            
            guess = int(input("Guess the number = "))
            counter += 1

            if guess == guess_number_easy:
                print("Corrects")
                print("-"*25)
                break
            
            elif counter == counter_number_easy:
                print(" Opps Try again ")
                print("-"*25)
                break

            else:
                print("Number ngani lang")

    elif choice == 2:

        print("You pick medium , Let me test you")
        print("The system gives you", counter_number_medium)

        while True:
            
            guess = int(input("Guess the number = "))
            counter += 1

            if guess == guess_number_medium:
                print("Corrects")
                print("-"*25)
                break
            
            elif counter == counter_number_medium:
                print(" Opps Try again ")
                print("-"*25)
                break

            else:
                print("Number ngani lang")

    elif choice == 3:

        print("You pick Hard , Let me test you")
        print("The system gives you", counter_number_hard)

        while True:
            
            guess = int(input("Guess the number = "))
            counter += 1

            if guess == counter_number_hard:
                print("Corrects")
                print("-"*25)
                break
            
            elif counter == counter_number_hard:
                print(" Opps Try again ")
                print("-"*25)
                break
            else:
                print("Number ngani lang")

    else:
        print("Thank you for playing")
        break



