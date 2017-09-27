import random
Colors=["red","green","blue","white","cyan","magenta","yellow","black","pink","brown","orange","purple","fuchsia"]
nums=[]
anagram=[]
n=len(Colors)-1
x=random.randint(1,n)
Chosen=Colors[x]
word=""
anagram=list(Chosen)
c=len(anagram)-1
while True:
    num=random.randint(0,c)
    if num in nums:
        pass
    else:
        word+=anagram[num]
        nums.append(num)
    if len(word)==len(Chosen):
        break
print("The anagram is ",word)
respuesta=input("Try to guess the color!: ")
while respuesta!= Chosen:
    respuesta=input("Noope, try again please: ")
if respuesta==Chosen:
    print("Yeah! It was ",Chosen,", well Done!")
