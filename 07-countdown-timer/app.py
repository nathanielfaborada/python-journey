import time
import os
def countdown_timer(countdown):

    while countdown > 0:
        os.system('cls')
        print(countdown)
        
    
        time.sleep(1)

        countdown -= 1
    os.system('cls')
    print("Times up")


try:
    countdown = int(input("How many seconds to countdown"))
    countdown_timer(countdown)

except ValueError:
    print("Please enter a valid number!")