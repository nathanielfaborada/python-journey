import random
def idagdag(unang_numero, pangalawang_numero):
    return unang_numero + pangalawang_numero

def ibawas(unang_numero, pangalawang_numero):
    return unang_numero - pangalawang_numero

def paramihin(unang_numero, pangalawang_numero):
    return unang_numero * pangalawang_numero

def hatiin(unang_numero, pangalawang_numero):
    return unang_numero / pangalawang_numero


print("-"*25)
print("Calculator")

# una = random.randint(1,100)
# pangalawa = random.randint(1,100) 
# print("Random first number = ", una)
# print("Random Second Numer = ", pangalawa)

una = int(input("Ilagay mo ang unang numero = "))
pangalawa = int(input("Ilagay mo ang pangalawang numero = "))
print("-"*25)

while True:
    print("Pindotin mo (+) para idagdag")
    print("Pindotin mo (-) para ibawas")
    print("Pindotin mo (x) para paramihin")
    print("Pindotin mo (/) para hatiin")
    print("-"*25)

    choice = input("Pumili ka na kaibigan : ")

    if choice == '+':
        Kabuuan = idagdag(una, pangalawa)

        print(f'{una} + {pangalawa} = {Kabuuan}')
        break

    elif choice == '-':
        kaibahan = ibawas(una, pangalawa)
        print(f'{una} + {pangalawa} = {kaibahan}')
        break

    elif choice == 'x': 
        Produkto = paramihin(una , pangalawa)
        print(f'{una} + {pangalawa} = {Produkto}')
        break

    elif choice == '/':
        if pangalawa == 0:
            print("Hindi pwedeng hatiin sa zero")
            print("-"*25)
            break
        

        else:
            Bahagimbilang = hatiin(una, pangalawa)
            print(f'{una} + {pangalawa} = {Bahagimbilang}')
            break   





