def Max(x,y):
    if x<=y:
        return y
    else :
        return x

print("This program will return the max value you enter!")
num1=int(input("Please enter the first value: "))
num2=int(input("Please enter the second value: "))
print("The max value is",Max(num1,num2))
