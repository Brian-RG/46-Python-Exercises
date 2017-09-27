import functools
def max_in_list(lista):
    return functools.reduce(lambda x,y: x if x>y else y,lista)

lista=[]
print("This program will return the max value of a list of numbers you give, write 'break' to finish")
while True:
    num=input("Introduce a number: ")
    if num=="break":
        break
    else:
        num=int(num)
        lista.append(num)

print(max_in_list(lista))
