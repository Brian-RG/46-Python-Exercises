import random
import Functions
def brackets_creation(x):
    brack=[]
    i=0
    while i < x:
        brack.append("[")
        brack.append("]")
        i+=1
    random.shuffle(brack)
    string="".join(brack)
    return string
def Check(bracks):
    lista=[]
    if bracks[0]=="]":
        return False
    else:
        for y in bracks:
            if y=="[":
                lista.append(y)
            elif y=="]" and len(lista)==0:
                return False
            elif y=="]":
                lista.pop()
    if len(lista)==0:
        return True
    else:
        return False
num=input("Introduce the number of brackets: ")
if Functions.int_valid(num) == True:
    lines=input("Introduce the number of lines: ")
    if Functions.int_valid(lines)==True:
        #Program
        lines=int(lines)
        num=int(num)
        l=0
        while l<lines:
            b=brackets_creation(num)
            if Check(b):
                print(b,"OK!")
            else:
                print(b, "Not Ok :(")
            l+=1
    else:
        print("Error")
