import random
num=random.randint(1,20)
intento=0
eleccion=int(input("I have chosen a number between 1 and 20, try to guess it!: "))
intento+=1
while True:
    if eleccion==num:
        print("Yeah! That's my number!! You did it in ",intento," guesses")
        break
    elif eleccion<num:
        eleccion=int(input("Nope, my number is bigger! Try Again!: "))
        intento+=1
    elif eleccion>num:
        eleccion=int(input("Nope, my number is lower! Try Again!: "))
        intento+=1
