def Celsius_to_Fahrenheit(to_convert):
    output = to_convert * 9 / 5
    final_output = output + 32

    print(f'{to_convert}°C is equal to {final_output}°F')


def Fahrenheit_to_Celsius(to_convert):
    output = to_convert - 32
    final_output = output * 5 / 9

    print(f'{to_convert}°F is equal to {final_output}°C')

while True:
    print("Temperature Converter")
    print("Enter 1 for Celsius-to-Fahrenheit ")
    print("Enter 2 for Fahrenheit-to-Celsius")
    print("Enter 3 to exit")
    choices = int(input("Enter you want to do = "))

    if choices == 1:
        print("Celsius-to-Fahrenheit")
        try:
            to_convert = float(input("Enter temperature in Celsius: "))
            Celsius_to_Fahrenheit(to_convert)
            break
        except ValueError:
            print("Enter only a number")

    elif choices == 2:
        print("Fahrenheit-to-Celsius")
        try:
            to_convert = float(input("Enter temperature in Fahrenheit: "))
            Fahrenheit_to_Celsius(to_convert)
            break
        except ValueError:
            print("Enter only a number")
        
    elif choices == 3:
        print("Thank you")
        break



