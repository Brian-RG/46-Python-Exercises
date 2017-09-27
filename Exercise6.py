def Sum(x):
   suma=0
   for i in range(0,len(x)):
       suma+=x[i]
   return suma

Lista=[]
print("This program will return the sum of a list of numbers you give")
value= True
c=1
while(value):
    if c==1:
        c+=1
        num=int(input("Introduce your number: "))
        Lista.append(num)
    else:
        print("Do you want to introduce another number? ")
        print("a)Yes")
        print("b)No")
        answer=input("")
        if answer=="a":
            nume=int(input("Introduce your number: "))
            Lista.append(nume)
        elif answer=="b":
            value=False

print("The sum of your list is ",Sum(Lista))
