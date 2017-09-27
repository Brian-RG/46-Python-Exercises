def Max_Of_Three(x,y,z):
    if x<=y<=z or y<=x<=z :
        return z
    elif y<=z<=x or z<=y<=x:
        return x
    elif x<=z<=y or z<=x<=y:
        return y

#MAIN

print("This program will return the max value of three numbers you introduce")
num1=int(input("Please, introduce the first number: "))
num2=int(input("Please, now introduce the second number: "))
num3=int(input("Now, please introduce the third number: "))
print("The biggest value of the three numbers you entered is ",Max_Of_Three(num1,num2,num3))
