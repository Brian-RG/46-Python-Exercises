def histogram(lista):
    a=len(lista)
    for b in lista:
        line=""
        c=0
        while c<b:
            c+=1
            line+="*"
        print(line)


#main
arr=[]
print("This program will make an histogram with the numbers you introduce")
print("Introduce the numbers of * you want per each line")
print("Write 'stop' to finish")
while True:
    num=input("Introduce the numbers of * you want in this line: ")
    if num=="stop":
        break
    else:
        num=int(num)
        arr.append(num)
histogram(arr)
