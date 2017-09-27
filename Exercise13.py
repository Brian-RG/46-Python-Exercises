def max_in_list(lista):
    return max(lista)

lista=[]
print("This program will return the highest number in a list you introduce. Write 'break' to finish")
while True:
    num=input("Introduce a number: ")
    if num=="break":
        break
    else:
        num=int(num)
        lista.append(num)
print (max_in_list(lista))
